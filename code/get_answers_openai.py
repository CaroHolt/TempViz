import openai

import fire
import time
import pandas as pd
import os
from retrying import retry
from decouple import config
from tqdm import tqdm
from tqdm.contrib.concurrent import thread_map
from few_shot_examples import *
import base64
tqdm.pandas()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    




class GPTWrapper:
    def __init__(self, gen_model, api_key=None):
        self.model_name = gen_model
        self.client = openai.OpenAI(api_key='<API-KEY>')


    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000) 
    def get_completion(self, prompt, image_path, few_shot, instruct, category):

        base64_image = encode_image(image_path)

        instruction = """As a professional "Text-to-Image" quality assessor, your task is to judge the performance of a
                text-image model w.r.t. a certain criteria by evaluating the image generated from a specific prompt.\n\n
                The criteria for evaluation are as follows:\n
                Rubrics:\n
                'Assess how accurately the image reflects the given prompt. Check if the object attributes along with all temporal elements—such as signs of aging in animals, 
                historical map borders, seasonal indicators in landscapes, lighting and shadows for time of day, architectural features that change over time, and stylistic 
                traits of artworks from different epochs—are correctly represented.'\n
                Please analyze step by step and provide the RATING using
                the following scale: ["Extremely Poor", "Poor", "Fair", "Good", "Very Good", "Outstanding"]. In this scale,
                "Extremely Poor" represents the worst alignment quality, and "Outstanding" represents the best
                alignment quality.\n
                Please do not generate any other opening, closing, and explanations. The output of the analysis and
                rating should be strictly adhered to the following format:\n
                ANALYSIS: Provide your analysis here\n
                RATING: Only provide your rating here."""
        
        instruction = "You are a helpful assistant."


        input = [
        {
            "role": "system",  
            "content": [
                {"type": "text", "text": instruction},
            ],
        }]
        
        if few_shot: 
            if instruct: 
                input += EXAMPLES_INSTRUCT_GPT[category] 
            if not instruct: 
                input += EXAMPLES_NO_INSTRUCT_GPT[category] 


        input.append({
            "role": "user",
            "content": [
                { "type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        })

        try:
            response = self.client.chat.completions.create(
                model = self.model_name,
                messages = input,
                #temperature=0.7,
                #top_p=0.9,
                #max_completion_tokens = 20
                )

            return response.choices[0].message.content
        
        except Exception as e:
            print(f"OpenAIError: {e}. Retrying with exponential backoff.")
            raise e

    def get_parallel_completions(self, prompts, audios, categories, few_shot, instruct, max_workers=4):
        completions = thread_map(self.get_completion, prompts, audios, categories, few_shot, instruct, max_workers=max_workers)
        return [c for c in completions]



def main(gen_model: str, 
         input_path: str, output_path:str,
         task: str, caching_path: str,
         n_batches: int, start_batch: int, 
         few_shot:bool, 
         instruct:bool,
         n_samples: int = 0,
         max_workers: int = 1, seed: int = 1234):
    
    # load csv
    df = pd.read_csv(input_path)
    print(f"Loaded data from {input_path}: {df.shape[0]} rows")

    # optional: select random sample from entries -- useful for debugging
    if n_samples > 0:
        df = df.sample(n_samples, random_state=seed)
        print(f"Sampled {n_samples} rows from data")

    # split df into n_batches, even if n_batches does not divide df evenly
    df_dict = {}
    for i in range(n_batches):
        df_dict[i] = df.iloc[i::n_batches].copy()

    # initialize GPTWrapper
    gpt = GPTWrapper(gen_model)
    print(f"Initialized OpenAI model: {gen_model}")

    if task == 'annotation_prompt':
        tasks = [f'annotation_prompt_0', 'annotation_prompt_2']
    else: 
        tasks = [task]

    for input_col in tasks: 

        output_col = f'model_response_{input_col}'

        # for each batch from start_batch, get completions and save to csv
        for i in range(start_batch, n_batches):
            print(f"Processing batch {i+1} of {n_batches} with {max_workers} workers")
            df_dict[i][output_col] = gpt.get_parallel_completions(df_dict[i][input_col], df_dict[i]['image_urls'], df_dict[i]['category'], few_shot, instruct, max_workers = max_workers)
            if not df_dict[i].empty:
                df_dict[i].to_csv(caching_path + f"/batch_{i}.csv", index=False)

        # concatenate all batches from the caching path
        df = pd.concat([pd.read_csv(caching_path + f"/batch_{i}.csv") for i in range(n_batches)])

        # write model name to column
        df["model_name"] = gen_model

        if not os.path.exists(output_path.rsplit("/", 1)[0]):
            os.makedirs(output_path.rsplit("/", 1)[0])

        if n_samples > 0:
            print(df[output_col])
        else:
            # save final dataframe to csv
            df.to_csv(output_path, index=False)
    
    return


if __name__ == "__main__":
    st = time.time()
    fire.Fire(main)
    et = time.time()
    print(f'Execution time: {et - st:.2f} seconds')
