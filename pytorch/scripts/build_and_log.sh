#!/usr/bin/env bash
mkdir -p ~/logs/
touch ~/logs/pytorch.log
MAX_JOBS=$(expr $(nproc) / 2) python setup.py build 2>&1 | tee ~/logs/pytorch.log
