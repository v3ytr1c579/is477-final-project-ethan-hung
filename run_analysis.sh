#!/bin/bash
set -e

python3 -m jupyter nbconvert \
  --to notebook \
  --execute notebooks/analysis.ipynb \
  --output analysis_executed.ipynb \
  --output-dir notebooks