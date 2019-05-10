#!/bin/bash

export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
export DEBUG=0
export CUDA_DEVICE_DEBUG=0
