# Creating the environment

- run script #1 just if your machine needs these libraries
- install miniconda
- run script #2 if your conda is not in the $PATH
- run script #3a to create your conda environment (change the name inside the script)
- run script #3b to install some building dependencies
- clone your fork of pytorch project
- activate your conda environment
- run script #4 to add some ENV variables by building scripts
- inside pytorch project, run script #5 to update submodules

# activating the environment

- run script #2 if your conda is not in the PATH
- activate your conda environment
- run script #4 to add som ENV variables used by building scripts
- run script #5 if your branch was updated

# bulding

- you can build using `python setup.py build`
- you can install pytorch from source in development mode using `python setup.py develop`
- you can rebuild just using `python setup.py build`

# test

- you can install pytest-xdist if you want to parallelize your tests
- ex how to test:
  - pytest test/test_nn.py::TestNN -vv
  - pytest test/test_nn.py::TestNN::test_interpolate_trilinear_3d_cuda -vv
