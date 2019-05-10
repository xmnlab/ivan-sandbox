#!/usr/bin/env bash
# it needs some investigation to use ccache from conda-forge

# install ccache
sudo apt install ccache

# update symlinks and create/re-create nvcc link
sudo /usr/sbin/update-ccache-symlinks
sudo ln -s /usr/bin/ccache /usr/lib/ccache/nvcc

# config: cache dir is ~/.ccache, conf file ~/.ccache/ccache.conf
# max size of cache
ccache -M 25Gi  # -M 0 for unlimited
# unlimited number of files
ccache -F 0

# deploy (and add to ~/.bashrc for later)
export PATH="/usr/lib/ccache:$PATH"
