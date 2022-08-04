#!/bin/zsh

$(which python3) -m pip install --upgrade pip

# $CONDA_PREFIX/bin/python3 -m pip install --upgrade pip

pip install wheel -y

python3 setup.py sdist bdist_wheel bdist_egg

pip install ./dist/my_minipack-1.0.0-py3-none-any.whl --force-reinstall

echo "done\n"
