#!/bin/bash

# set -ex

export CONDA_ENV_NAME=pytorch-$(whoami)
conda create -n $CONDA_ENV_NAME -y python=3.6

source activate $CONDA_ENV_NAME

conda install -y -n $CONDA_ENV_NAME cudatoolkit-dev=10.0
conda install -y -n $CONDA_ENV_NAME numpy ninja  pyyaml mkl mkl-include setuptools cmake cffi typing
conda install -y -n $CONDA_ENV_NAME -c pytorch magma-cuda100
pip install pytest pytest-xdist
