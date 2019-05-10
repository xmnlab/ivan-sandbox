#!/usr/bin/env bash
mkdir -p ~/logs/
touch ~/logs/pytorch.log
python setup.py build 2>&1 | tee ~/logs/pytorch.log
