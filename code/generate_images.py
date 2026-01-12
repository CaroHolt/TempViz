import torch
import os
import pandas as pd
import time 
import fire
import logging
from diffusers import Kandinsky3Pipeline, AutoPipelineForText2Image, DiffusionPipeline, StableDiffusionPipeline, StableDiffusion3Pipeline, AltDiffusionPipeline, DPMSolverMultistepScheduler, FluxPipeline

from tqdm import tqdm
import glob


def main(
        # data parameters
        test_data_input_path: str,
        input_col: str,
        test_data_output_path: str,

        # model parameters
        cache_dir:str,
        model_name:str

        ):

    ###########################################################
    # LOAD DATA
    ###########################################################

    # load TEST data
    if 'csv' in test_data_input_path:
        test_df = pd.read_csv(test_data_input_path)
    elif 'xlsx' in test_data_input_path:
        test_df = pd.read_excel(test_data_input_path)

    print(test_data_input_path)
    print(f"Loaded TEST data: {test_df.shape[0]} rows")

    seed = 42

    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    if 'sdxlbase' in model_name:
        print('Loading model sdxlbase')
        pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", variant="fp16", torch_dtype=torch.float16, cache_dir=cache_dir)
        pipeline = pipeline.to("cuda")
    elif 'sdxlturbo' in model_name:
        print('Loading model sdxlturbo')
        pipeline = DiffusionPipeline.from_pretrained("stabilityai/sdxl-turbo", variant="fp16", torch_dtype=torch.float16, cache_dir=cache_dir)
        pipeline = pipeline.to("cuda")
    elif 'sdv15' in model_name:
        print('Loading model sdv15')
        pipeline = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", variant="fp16", torch_dtype=torch.float16, cache_dir=cache_dir)
        pipeline = pipeline.to("cuda")
    elif 'stable-diffusion-3-5' in model_name:
        print('Loading model Stable Diffusion-3')
        pipeline = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3.5-large", torch_dtype=torch.float16, cache_dir=cache_dir)
        pipeline = pipeline.to("cuda")
    elif 'blackforest' in model_name:
        print('Loading model Blackforest')
        pipeline = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-dev",
            torch_dtype=torch.bfloat16, 
            cache_dir=cache_dir)
        pipeline = pipeline.to("cuda")




    # check if output path exists, otherwise create it
    if not os.path.exists(test_data_output_path.rsplit("/", 1)[0]):
        logging.info(f"Creating new path {test_data_output_path.rsplit('/', 1)[0]}")
        os.makedirs(test_data_output_path.rsplit("/", 1)[0])

    pipeline.set_progress_bar_config(disable=True)


    for index, row in tqdm(test_df.iterrows()):
        if (len(glob.glob(f"{test_data_output_path}image_{str(row['index'])}_.png")) != 1):

            image = pipeline(row['prompt']).images[0]

            imagetitle = 'image_' + str(row['index']) + '.png'


            image.save(test_data_output_path + imagetitle)

        

       


if __name__ == "__main__":
    st = time.time()
    fire.Fire(main)
    logging.info(f'Total execution time: {time.time() - st:.2f} seconds')