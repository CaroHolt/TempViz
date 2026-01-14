import pandas as pd
import time 
import fire
import logging
import torch
import os
import glob

import requests
from PIL import Image
import copy
from secrets import token_hex
from tqdm import tqdm
import transformers
from transformers import AutoProcessor, AutoModelForVision2Seq, BitsAndBytesConfig, AutoModel, AutoTokenizer
from random import sample
from few_shot_examples import *
from qwen_vl_utils import process_vision_info

print("versions:",
      "torch", torch.__version__,
      "transformers", transformers.__version__)



def resize_images(img_list, max_dim=448):
    resized = []
    for img in img_list:
        w, h = img.size
        scale = min(max_dim / w, max_dim / h)
        new_size = (int(w * scale), int(h * scale))
        resized.append(img.resize(new_size, Image.Resampling.LANCZOS))
    return resized


def main(
        # data parameters
        model: str,
        test_data_output_path: str,

        test_data_input_path: str,

        prompt_strategy: str,

        # model parameters
        model_name_or_path: str,

        cache_dir:str,
          
        # quantization parameters
        load_in_8bit: bool,

        few_shot: bool,

        batch_size: str,
           
        # misc parameters
        log_level: str,

        sample_size:int

        ):

    ###########################################################
    # SET UP
    ###########################################################

     # set up logging
    logging.basicConfig(level=getattr(logging, log_level.upper()), format='%(asctime)s %(levelname)s %(message)s')

        # set up device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logging.info(f"Running on device: {device}")
    if device == "cuda":
        logging.info(f"CUDA memory: {round(torch.cuda.mem_get_info()[0]/1024**3,2)}GB")

    ###########################################################
    # LOAD DATA
    ###########################################################

    # load TEST data
    if prompt_strategy == 'llm_questions':
        df = pd.read_csv('llm_prompts/prompts_' + test_data_input_path)
    else:
        df = pd.read_csv(test_data_input_path)


    
    processor = AutoProcessor.from_pretrained(model_name_or_path, padding_side='left', cache_dir=cache_dir)
    model = AutoModelForVision2Seq.from_pretrained(model_name_or_path,
                                                    dtype=torch.float16,
                                                    trust_remote_code=True,
                                                    cache_dir=cache_dir,
                                                    device_map='auto')
    


    if prompt_strategy in ['annotation_questions', 'llm_questions', 'instruct']:

        # Load all messages
        image_urls = df['image_urls'].tolist() 
        if sample_size > 0:
            image_urls = sample(image_urls, sample_size)


        images = []
        for url in image_urls: 
            image = Image.open(url)
            keep = image.copy()
            images.append(keep)
            image.close()


        # Gather prompts and create instructions
        instruction = "You are a helpful assistant."

        if prompt_strategy == 'annotation_questions':
            prompt_cols = ['annotation_prompt_0', 'annotation_prompt_1', 'annotation_prompt_2']
        elif prompt_strategy == 'instruct':
            prompt_cols = ['vlm_prompt']
            instruction = """As a professional "Text-to-Image" quality assessor, your task is to judge the performance of a
                text-image model w.r.t. a certain criteria by evaluating the image generated from a specific prompt.\n\n
                The criteria for evaluation are as follows:\n
                Rubrics:\n
                'Assess how accurately the image reflects the given prompt. Check if the object attributes along with all temporal elements—such as signs of aging in animals, 
                historical map borders, seasonal indicators in landscapes, lighting and shadows for time of day, architectural features that change over time, and stylistic 
                traits of artworks from different epochs—are correctly represented.'\n
                Please analyze step by step and provide the RATING using
                the following scale: ["Not accept", "Accept]. In this scale,
                "Not accept" represents images that do not accurately reflect the prompt."Accept" represents images that do accurately reflect the prompt along and also the temporal elements.\n
                Please do not generate any other opening, closing, and explanations. The output of the analysis and
                rating should be strictly adhered to the following format:\n
                ANALYSIS: Provide your analysis here\n
                RATING: Only provide your rating here."""
                    

        elif prompt_strategy == 'llm_questions':
            prompt_cols = [x for x in df.columns if 'quest' in x]

            prompt_cols = [x for x in prompt_cols if not 'questions' in x]
            print(prompt_cols)


        # Loop over different prompts if multiple
        for prompt in prompt_cols:

            if few_shot:
                templated_msgs = []
                for text, category, image_url in zip(df[prompt].tolist(), df['category'].tolist(), df['image_urls'].tolist()):
                    # build the message block for this text
                    conv = copy.deepcopy(EXAMPLES_INSTRUCT[category]) + [
                        {"role": "system", "content": instruction},
                        {
                        "role": "user",
                        "content": [
                            {"type": "image", "image": image_url},     
                            {"type": "text", "text": text},
                    ]}]
                    
                    templated_msgs.append(conv)    
            


                responses = []
                for i in tqdm(range(0, len(templated_msgs), batch_size), desc="Processing batches"):
                    batch_prompts = templated_msgs[i:i + batch_size]

                    input_texts = []
                    batch_image_lists = [] 

                    for conv in batch_prompts:

                        txt = processor.apply_chat_template(
                            conv,
                            tokenize=False,
                            add_generation_prompt=True
                        )
                        input_texts.append(txt)


                        imgs, _ = process_vision_info(conv)   
                        imgs = resize_images(imgs, max_dim=448)
                        batch_image_lists.append(imgs)

                    if any(len(lst) > 0 for lst in batch_image_lists):
                        inputs = processor(
                            text=input_texts,
                            images=batch_image_lists,    
                            return_tensors="pt",
                            padding=True,
                            truncation=True
                        )
                    else:
                        inputs = processor(
                            text=input_texts,
                            return_tensors="pt",
                            padding=True,
                            truncation=True
                        )

                    inputs = inputs.to(device)

                    # Generate
                    output_ids = model.generate(**inputs, max_new_tokens=1024)
                    generated_ids = [
                        output_ids[len(input_ids) :]
                        for input_ids, output_ids in zip(inputs.input_ids, output_ids)
                    ]
                    generated_texts = processor.batch_decode(
                        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
                    )
                    responses.extend(generated_texts)

            if not few_shot:

                templated_msgs = []
                for text in df[prompt].tolist():

                    messages = [
                        {"role": "system", "content": instruction},
                        {
                            "role": "user",
                            "content": [
                                {"type": "image"},                
                                {"type": "text", "text": text},
                            ],
                        }
                    ]
                    
                    templated_msgs.append(messages)    
            

                # Batch process prompts
                responses = []
                for i in tqdm(range(0, len(templated_msgs), batch_size), desc="Processing batches"):
                    batch_images = images[i:i + batch_size]  
                    batch_prompts = templated_msgs[i:i + batch_size]

                    input_texts = [
                        processor.apply_chat_template(
                            conv,                                  
                            tokenize=False,
                            add_generation_prompt=True
                        )
                        for conv in batch_prompts              
                    ]

                    inputs = processor(text=input_texts, images=batch_images, return_tensors="pt", padding=True)

                    inputs = inputs.to(device)

                    # Generate
                    output_ids = model.generate(**inputs, max_new_tokens=1024)
                    generated_ids = [
                        output_ids[len(input_ids) :]
                        for input_ids, output_ids in zip(inputs.input_ids, output_ids)
                    ]
                    generated_texts = processor.batch_decode(
                        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
                    )
                    responses.extend(generated_texts)


            if sample_size == 0:
                if os.path.exists(test_data_output_path): 
                    df = pd.read_csv(test_data_output_path)

                # write new model completions to new column
                df["model_name"] = model_name_or_path
                df[f"model_prompt_{prompt}"] = df[prompt].tolist()
                df[f"model_response_{prompt}"] = responses

                # check if output path exists, otherwise create it
                if not os.path.exists(test_data_output_path.rsplit("/", 1)[0]):
                    logging.info(f"Creating new path {test_data_output_path.rsplit('/', 1)[0]}")
                    os.makedirs(test_data_output_path.rsplit("/", 1)[0])

                logging.info(f"Saving completions to {test_data_output_path}")
                df.to_csv(test_data_output_path, index=False)

            else: 
                print(responses)




        

    

    


if __name__ == "__main__":
    st = time.time()
    fire.Fire(main)
    logging.info(f'Total execution time: {time.time() - st:.2f} seconds')











