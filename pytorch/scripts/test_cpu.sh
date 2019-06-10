#!/usr/bin/env bash
mkdir -p ~/logs/
touch ~/logs/pytorch_test.log
pytest -vv -n $(nproc) test/test_nn.py  2>&1 | tee ~/logs/pytorch_test.log
