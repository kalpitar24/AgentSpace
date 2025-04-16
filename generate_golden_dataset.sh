#!/bin/bash

cd ../golden_dataset_gen || exit

python generate_golden_dataset.py \
  --input_folder ../rag-agent/your_docs \
  --output_file ../rag-agent/golden_dataset/golden_set.json

cd ../rag-agent

echo "Golden dataset created in golden_dataset/golden_set.json"
