#!/bin/bash

# UV Installation
echo "UV Installation..."
curl -sSLf https://astral.sh/uv/install.sh | sh

# Checking for uv
if ! command -v uv &>/dev/null; then
    echo "Error! UV is not set."
    exit 1
fi

# Launching the program main.py
echo "Launch main.py..."
uv run main.py
