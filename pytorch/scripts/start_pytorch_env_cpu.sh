#!/usr/bin/env bash
source ./source/2_add_miniconda_to_path.sh
source ./source/4a_startup_pytorch_conda_env.sh
source ./source/4b_startup_pytorch.sh
export NO_CUDA=1
export USE_CUDA=0
export DEBUG=1
