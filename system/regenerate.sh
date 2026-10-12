#!/usr/bin/env bash

set -e 

cd "$(dirname "$0")"

source "$(dirname "$0")/.venv/bin/activate"

make regenerate
