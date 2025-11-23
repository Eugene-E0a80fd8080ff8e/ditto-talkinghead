#!/bin/bash

cd ..

python scripts/cvt_blackwell.py --onnx_dir "./checkpoints/ditto_onnx" --trt_dir "./checkpoints/ditto_trt_blackwell"