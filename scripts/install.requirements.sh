#!/usr/bin/env bash

SCRIPT_PATH="$(cd "$(dirname "$0")"; pwd -P)"

python -m pip freeze | grep --quiet scikit-learn
if [[ $? -eq 1 ]]; then
    cd ${SCRIPT_PATH}/..
    python -m pip install --no-cache-dir -e .
fi
