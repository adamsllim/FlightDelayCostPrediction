import os
import pandas as pd

# Path to dataset (update based on extracted files)
DATASET_DIR = os.path.expanduser("~/.cache/kagglehub/datasets/robikscube/flight-delay-dataset-20182022/versions/4")

# List available files
files = os.listdir(DATASET_DIR)
print(f"Available dataset files: {files}")
