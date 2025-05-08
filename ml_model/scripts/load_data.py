# ml_model/scripts/load_data.py

import pandas as pd
import os

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

matches_path = os.path.join(DATA_DIR, 'matches.csv')
deliveries_path = os.path.join(DATA_DIR, 'deliveries.csv')

# Load datasets
matches_df = pd.read_csv(matches_path)
deliveries_df = pd.read_csv(deliveries_path)

# Show previews
print("=== Matches Data ===")
print(matches_df.head(), "\n")

print("=== Deliveries Data ===")
print(deliveries_df.head())
