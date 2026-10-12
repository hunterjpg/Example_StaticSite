#!/usr/bin/env bash

set -e 

cd "$(dirname "$0")"

source "$(dirname "$0")/.venv/bin/activate"

"$(dirname "$0")/.venv/bin/pelican" content
