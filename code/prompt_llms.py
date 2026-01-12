import pandas as pd
import time 
import fire
import logging
import torch
import os
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM

def main(
        # data parameters
        test_data_input_path: str,
        n_test_samples: int,
        input_col: str,
        test_data_output_path: str,

        # model parameters
        model_name_or_path: str,
        cache_dir:str,

        # inference parameters
        batch_size, 
          
        # quantization parameters
        load_in_8bit: bool,
           
        # misc parameters
        log_level: str,

        device_map: str
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
    test_df = pd.read_csv(test_data_input_path)
    logging.info(f"Loaded TEST data: {test_df.shape[0]} rows")

    # optional: select random sample of rows for TEST -- useful for debugging
    if n_test_samples > 0:
        test_df = test_df.sample(n_test_samples, random_state=123)
        logging.info(f"Sampled {n_test_samples} rows from TEST data")


    test_df['extract_caption'] = test_df[input_col].replace('Produce ', '').replace('Give me ', '').replace('Create ', '').replace('Generate ', '').replace('a photorealistic image of', '')
    


    template = ("Given an image description, generate multiple-choice questions that can verify if the image description is correct for an image.\n\n"
                "First extract elements from the image description."
                "Then classify each element into a category (object, human, animal, food, activity, attribute, counting, color, material, spatial, location, shape, other)." 
                "Finally, generate different questions for each element, open-ended and multiple choice and also the correct answer. For example: 'What is the main subject of the image? Answer: Pony'\n\n"
                "Description: '{}'")
    

    
    # Apply the template to each name in the list
    prompts =  [template.format(example) for example in test_df['extract_caption'].tolist()]

    conversations = []
    for prompt in prompts:
        conversations.append([
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ])
    

    # print 3 random prompts
    logging.info(f"3 random prompts from TEST data:\n{conversations[:3]}\n")

    ###########################################################
    # LOAD GENERATOR
    ###########################################################

    logging.info(f"Loading model {model_name_or_path}")

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path, 
                                                 device_map=device_map, 
                                                 torch_dtype=torch.float16, 
                                                 trust_remote_code=True,
                                                 cache_dir=cache_dir)
    
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token



    ###########################################################
    # GET COMPLETIONS
    ###########################################################

    logging.info(f"Generating completions for {len(conversations)} prompts")

    input_texts = [
        tokenizer.apply_chat_template(conv, 
                                     tokenize=False, 
                                     add_generation_prompt=True)
        for conv in conversations
    ]


    completions = []
    for i in tqdm(range(0, len(input_texts), batch_size)):
        input_batch = input_texts[i:i + batch_size]
        inputs = tokenizer(input_batch, return_tensors="pt", padding=True).to(device)

        with torch.no_grad():
            outputs = model.generate(
                input_ids=inputs["input_ids"],
                temperature=0.0001,
                max_new_tokens=1024,
                top_p=0.9, 
                top_k=100,
                do_sample=True
            )
            #outputs = model.generate(**inputs, max_new_tokens=256, do_sample=True, temperature=0.1, top_p=0.9, top_k=100)
        

        if 'Qwen' in model_name_or_path:
            generated_ids = [
                output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, outputs)
            ]

        else:
            generated_ids = outputs[:, inputs['input_ids'].size(1):]

        responses = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        completions.extend(responses)

    logging.info(f"Generated {len(completions)} completions")

    # write new model completions to new column
    test_df["prompt"] = conversations
    test_df["model_completion"] = completions
    test_df["model_name"] = model_name_or_path

    

    # check if output path exists, otherwise create it
    if not os.path.exists(test_data_output_path.rsplit("/", 1)[0]):
        logging.info(f"Creating new path {test_data_output_path.rsplit('/', 1)[0]}")
        os.makedirs(test_data_output_path.rsplit("/", 1)[0])

    test_df.to_csv(test_data_output_path, index=False)

    logging.info(f"Saving completions to {test_data_output_path}")
    if n_test_samples == 0:
        test_df.to_csv(test_data_output_path, index=False)
    else:
        print(completions)


if __name__ == "__main__":
    st = time.time()
    fire.Fire(main)
    logging.info(f'Total execution time: {time.time() - st:.2f} seconds')