import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # points to 'ml_model/'
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
PIPELINE_PATH = os.path.join(MODEL_DIR, 'final_pipeline.pkl')  # ✅ pipeline output

# Load data
X = pd.read_csv(os.path.join(DATA_DIR, 'X.csv'))
y = pd.read_csv(os.path.join(DATA_DIR, 'y.csv')).values.ravel()

# Define categorical and numerical columns
categorical_columns = ['team1', 'team2', 'toss_winner', 'toss_decision', 'venue']
numerical_columns = [col for col in X.columns if col not in categorical_columns]

# Handle missing values in numerical columns
X[numerical_columns] = X[numerical_columns].fillna(X[numerical_columns].mean())

# Create transformers
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numerical_transformer = StandardScaler()

# Combine into preprocessor
preprocessor = ColumnTransformer([
    ('cat', categorical_transformer, categorical_columns),
    ('num', numerical_transformer, numerical_columns)
])

# Create full pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit pipeline
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model trained. Accuracy on test set: {acc:.2f}")

# Save full pipeline
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(pipeline, PIPELINE_PATH)
print(f"✅ Full pipeline saved to '{PIPELINE_PATH}'")
