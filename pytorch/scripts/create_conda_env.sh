#!/usr/bin/env bash
current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "${current_dir}/source/2_add_miniconda_to_path.sh"
source "${current_dir}/source/3a_create_pytorch_env.sh"
source "${current_dir}/source/3b_install_conda_build_deps.sh"
