#!/bin/bash
set -e

echo "STEP 1: Checking data acquisition..."
python3 scripts/acquire_data.py

echo ""
echo "STEP 2: Verifying dataset integrity..."
python3 scripts/verify_data.py

echo ""
echo "STEP 3: Running analysis notebook..."

python3 -m jupyter nbconvert \
  --to notebook \
  --execute notebooks/analysis.ipynb \
  --output analysis_executed.ipynb \
  --output-dir notebooks

echo ""
echo "Workflow completed successfully."