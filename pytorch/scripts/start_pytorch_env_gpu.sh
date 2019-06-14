#!/usr/bin/env bash
current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "${current_dir}/source/2_add_miniconda_to_path.sh"
source "${current_dir}/source/4a_startup_pytorch_conda_env.sh"
source "${current_dir}/source/4b_startup_pytorch.sh"
alias nvcc='nvcc --resorce-usage'
export DEBUG=1
unset NO_CUDA
