#!/usr/bin/env bash

if [ $(uname) == Darwin ]; then
  MINICONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
else
  MINICONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
fi

DOWNLOAD_PATH=$HOME/tmp

wget -c -O $DOWNLOAD_PATH/miniconda.sh  $MINICONDA_URL

bash $DOWNLOAD_PATH/miniconda.sh -b -p $HOME/miniconda3
