#!/bin/sh


# check python version
python3 --version

export CUDA_VISIBLE_DEVICES=0

# store repo path
REPO="<PROJECT-REPO>"

for MODEL in  "blackforest"  ; do #"sdv15" "sdxlturbo" "sdxlbase" "stable-diffusion-3-5"

    for EXPERIMENT in "Time"; do #"Animals" "Artworks" "Buildings" "Maps" "Landscape"; do

        python3 generate_images.py \
            --model_name $MODEL\
            --test_data_input_path $EXPERIMENT.csv \
            --input_col "prompt" \
            --test_data_output_path $REPO/$MODEL/$EXPERIMENT/\
            --cache_dir $REPO/cache_dir

    done;


done;