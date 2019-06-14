#!/usr/bin/env bash
mkdir -p ~/logs/
touch ~/logs/pytorch_test.log
pytest -vv  test/test_nn.py  2>&1 | tee ~/logs/pytorch_test.log
