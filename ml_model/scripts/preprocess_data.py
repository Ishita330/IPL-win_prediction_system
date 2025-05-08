import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
matches_path = os.path.join(DATA_DIR, 'matches.csv')

# Load data
try:
    matches = pd.read_csv(matches_path)
    print(f"✅ Loaded data from {matches_path}")
except FileNotFoundError:
    raise FileNotFoundError(f"❌ Could not find the file {matches_path}. Please make sure the file exists.")

# Select relevant features
matches = matches[['team1', 'team2', 'toss_winner', 'toss_decision', 'venue', 'winner']]

# Drop rows with nulls or no result
initial_shape = matches.shape
matches.dropna(inplace=True)
matches = matches[matches['winner'] != '']

# Log how many rows were dropped
dropped_rows = initial_shape[0] - matches.shape[0]
if dropped_rows > 0:
    print(f"⚠️ Dropped {dropped_rows} rows due to missing values or no result.")

# Keep only common teams
common_teams = [
    'Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Rajasthan Royals', 'Delhi Capitals',
    'Sunrisers Hyderabad', 'Kings XI Punjab', 'Punjab Kings'
]
matches = matches[
    matches['team1'].isin(common_teams) &
    matches['team2'].isin(common_teams) &
    matches['winner'].isin(common_teams)
]

# Log rows dropped due to uncommon teams
final_shape = matches.shape
dropped_team_rows = initial_shape[0] - final_shape[0]
if dropped_team_rows > 0:
    print(f"⚠️ Dropped {dropped_team_rows} rows due to uncommon teams.")

# Split into features and labels WITHOUT encoding
X = matches.drop('winner', axis=1)
y = matches['winner']

# Save raw features and target
X.to_csv(os.path.join(DATA_DIR, 'X.csv'), index=False)
y.to_csv(os.path.join(DATA_DIR, 'y.csv'), index=False)

print("✅ Saved raw (non-encoded) X.csv and y.csv.")
