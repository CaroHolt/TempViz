#!/bin/sh


GEN_MODEL="gpt-5" #"gpt-4o-mini-2024-07-18"
REPO="<PROJECT-REPO>"
EXPERIMENT=vlm_annotation

python3 get_answers_openai.py \
    --gen_model $GEN_MODEL \
    --input_path $EXPERIMENT.csv \
    --output_path $REPO/$GEN_MODEL/{$EXPERIMENT}.csv \
    --task "annotation_prompt_2" \
    --caching_path $REPO/cache_dir \
    --n_batches 5 \
    --start_batch 0 \
    --max_workers 5 \
    --n_samples 0
