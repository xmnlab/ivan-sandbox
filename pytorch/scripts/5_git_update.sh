#!/bin/bash

git pull --rebase
git submodule sync --recursive
git submodule update --init --recursive

