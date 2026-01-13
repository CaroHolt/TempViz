from PIL import Image
import requests
from transformers import AutoProcessor, AutoModel, AutoTokenizer, BlipForConditionalGeneration, BlipProcessor
import torch
import glob
import os
import logging
import pandas as pd
from tqdm import tqdm
from torchmetrics.functional.multimodal import clip_score
from functools import partial
import time 
import fire
from sentence_transformers import SentenceTransformer, util




def main(
        task:str,

        ):
    
    REPO_NAME="<REPO-PATH>"

    cache_dir = f'{REPO_NAME}/cache_dir'

    if task == 'clip':
        model_name = "laion/CLIP-ViT-bigG-14-laion2B-39B-b160k"
        clip_model = AutoModel.from_pretrained(model_name, cache_dir=cache_dir).to('cuda:3')
        processor = AutoProcessor.from_pretrained(model_name, cache_dir=cache_dir)
    elif task == 'caption':
        model_name = "Salesforce/blip-image-captioning-base"
        caption_model = BlipForConditionalGeneration.from_pretrained(model_name).to('cuda:3')
        processor = BlipProcessor.from_pretrained(model_name)
        model_sentence = SentenceTransformer('all-MiniLM-L6-v2')
    

    for category in ["Landscapes", "Animals", "Artworks", "Buildings", "Maps"]:
        print(category)
        df = pd.read_csv(f'{category}.csv')
        for model in tqdm(['sdv15', 'sdxlbase', 'sdxlturbo', 'blackforest', 'stable-diffusion-3-5']):
            all_rows = []
            for index, row in df.iterrows():
                dict_row = {}
                dict_row['category'] = category
                dict_row['model'] = model
                dict_row['index'] = str(row['index'])
                prefix_path = f'/work/bbc6523/BA_images/{model}/{category}/'
                image_name = 'image_' + str(row['index']) + '.png'
                full_image_path = prefix_path + image_name
                if task == 'clipscore':
                    try:
                        image = Image.open(full_image_path)
                        prompt = row['prompt'].replace('Produce ', '').replace('Give me ', '').replace('Create ', '').replace('Generate ', '')
                        prompt = prompt.replace('a photorealistic image of', '')
                        dict_row['prompt'] = row['prompt']
                        dict_row['text compare'] = prompt

                        inputs = processor(
                            text=prompt,
                            images=image,
                            return_tensors="pt",
                            padding=True
                        ).to('cuda:3')
                        outputs = clip_model(**inputs)

                        # Extract the embeddings
                        image_embeddings = outputs.image_embeds  # Image embedding
                        text_embeddings = outputs.text_embeds    # Text embedding

                        # Normalize the embeddings
                        image_embeddings = image_embeddings / image_embeddings.norm(dim=-1, keepdim=True)
                        text_embeddings = text_embeddings / text_embeddings.norm(dim=-1, keepdim=True)
                        
                        # Calculate the cosine similarity to get the CLIP score
                        clip_score = torch.matmul(image_embeddings, text_embeddings.T).item()

                        dict_row['clip_score'] = clip_score
                    except:
                        dict_row['clip_score'] = "error"
                        print(image_name)
                elif task == 'caption':
                    image = Image.open(full_image_path).convert('RGB')
                    inputs = processor(image, return_tensors="pt").to('cuda:3')
                    out = caption_model.generate(**inputs, max_length=200)
                    caption = processor.decode(out[0], skip_special_tokens=True)
                    dict_row['caption'] = caption
                    emb1 = model_sentence.encode(caption, convert_to_tensor=True)
                    prompt = row['prompt'].replace('Produce ', '').replace('Give me ', '').replace('Create ', '').replace('Generate ', '').replace('a photorealistic image of', '')
                    dict_row['prompt'] = prompt
                    emb2 = model_sentence.encode(prompt, convert_to_tensor=True)
                    similarity = util.cos_sim(emb1, emb2)
                    dict_row['cosine'] = similarity.item()



                all_rows.append(dict_row)
            df = pd.DataFrame(all_rows)
            new_df = pd.read_csv(f'{task}_scores_full.csv')
            new_df = pd.concat([df,new_df])
            new_df.to_csv(f'{task}_scores_full.csv', index=False)



if __name__ == "__main__":
    st = time.time()
    fire.Fire(main)
    logging.info(f'Total execution time: {time.time() - st:.2f} seconds')