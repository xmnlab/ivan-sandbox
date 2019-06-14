#!/usr/bin/env bash
mkdir -p ~/logs/
touch ~/logs/pytorch_test.log
pytest -vv -n $(expr $(nproc) / 4) test/test_nn.py  2>&1 | tee ~/logs/pytorch_test.log
