import kagglehub
import os

# Define dataset directory
DATASET_DIR = os.path.expanduser("~/.cache/kagglehub/datasets/robikscube/flight-delay-dataset-20182022")

# Check if dataset already exists
if not os.path.exists(DATASET_DIR):
    print("Dataset not found. Downloading...")
    path = kagglehub.dataset_download("robikscube/flight-delay-dataset-20182022")
    print(f"Dataset downloaded to: {path}")
else:
    print(f"Dataset already exists at: {DATASET_DIR}")