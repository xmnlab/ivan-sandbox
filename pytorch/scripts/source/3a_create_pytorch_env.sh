#!/bin/bash

export PYTHON_VERSION=3.6
export CONDA_ENV_NAME=pytorch-$(whoami)
conda create -n $CONDA_ENV_NAME -y python=$PYTHON_VERSION

source activate $CONDA_ENV_NAME

# conda install -y -n $CONDA_ENV_NAME cudatoolkit-dev=10.0  python=$PYTHON_VERSION
conda install -y -n $CONDA_ENV_NAME numpy pyyaml ninja mkl mkl-include setuptools cmake cffi typing  python=$PYTHON_VERSION
conda install -y -n $CONDA_ENV_NAME -c pytorch magma-cuda100
pip install pytest pytest-xdist

