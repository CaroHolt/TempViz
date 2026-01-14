#!/bin/sh


# check python version
python3 --version

# to surpress annoyingly verbose warning
export TOKENIZERS_PARALLELISM=true
export CUDA_VISIBLE_DEVICES=0,1,2,3

# store repo path
REPO="<PROJECT-REPO>"

# set params
PROVIDER=Qwen 
MODEL_NAME=Qwen2.5-VL-32B-Instruct
PROMPT_STRATEGY=annotation_questions #llm_questions annotation_questions instruct
FEW_SHOT=True


for EXPERIMENT in  "Artworks" "Buildings" "Maps" "Animals"; do # "Landscapes", "Animals", "Artworks", "Buildings", "Maps"

    for MODEL in "sdxlbase" "blackforest" "sdv15" "sdxlturbo" "stable-diffusion-3-5"; do # "sdxlbase" "blackforest" "sdv15" "sdxlturbo" "stable-diffusion-3-5"

        python3 prompt_vlm_models.py \
            --model_name_or_path $PROVIDER/$MODEL_NAME \
            --test_data_input_path $EXPERIMENT.csv \
            --prompt_strategy $PROMPT_STRATEGY \
            --model $MODEL \
            --test_data_output_path $REPO/vqa_results/$MODEL_NAME/$EXPERIMENT/$MODEL.csv \
            --load_in_8bit False \
            --batch_size 4 \
            --few_shot $FEW_SHOT \
            --log_level "error" \
            --cache_dir $REPO/cache_dir \
            --sample_size 0

    done;

done;