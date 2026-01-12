#!/bin/sh


# check python version
python3 --version

# to surpress annoyingly verbose warning
export TOKENIZERS_PARALLELISM=true
export CUDA_VISIBLE_DEVICES=0,1,2

# store repo path
REPO="<PROJECT-REPO>"


for PROVIDER in meta-llama; do

    for MODEL_NAME in Llama-3.3-70B-Instruct; do

        for EXPERIMENT in "Maps" "Buildings"; do

            python3 prompt_llms.py \
                --model_name_or_path $PROVIDER/$MODEL_NAME \
                --test_data_input_path $EXPERIMENT.csv \
                --n_test_samples 0 \
                --batch_size 12 \
                --input_col "prompt" \
                --test_data_output_path ../data/llm_prompts/prompts_$EXPERIMENT.csv \
                --log_level "debug" \
                --load_in_8bit False \
                --cache_dir $REPO/cache_dir \
                --device_map auto \

        done;

    done;


done;