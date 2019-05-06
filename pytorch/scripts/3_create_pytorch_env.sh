#!/bin/bash

# set -ex

conda create -n pytorch-xmn -y python=3.6

source activate pytorch-xmn

conda install -y -n pytorch-xmn cudatoolkit-dev=10.0
conda install -y -n pytorch-xmn numpy pyyaml mkl mkl-include setuptools cmake cffi typing
conda install -y -n pytorch-xmn -c pytorch magma-cuda100
pip install ninja
