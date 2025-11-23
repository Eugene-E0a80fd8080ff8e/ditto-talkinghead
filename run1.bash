#!/bin/bash

python inference.py \
    --data_root "./checkpoints/ditto_trt_blackwell" \
    --cfg_pkl "./checkpoints/ditto_cfg/v0.4_hubert_cfg_trt.pkl" \
    --audio_path "./example/audio.wav" \
    --source_path "./example/image.png" \
    --output_path "./tmp/result.mp4" 
