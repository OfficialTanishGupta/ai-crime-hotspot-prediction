import joblib
import numpy as np
import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model artifacts
model = joblib.load(os.path.join(BASE_DIR, "models/hotspot_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models/scaler.pkl"))

with open(os.path.join(BASE_DIR, "models/cluster_label_map.json")) as f:
    cluster_label_map = json.load(f)

def predict_hotspot(crime_count, latitude, longitude):
    """
    Predict AI-based crime hotspot level
    """
    X = pd.DataFrame(
        [[crime_count, latitude, longitude]],
        columns=["crime_count", "latitude", "longitude"]
    )

    X_scaled = scaler.transform(X)
    cluster = str(model.predict(X_scaled)[0])

    return cluster_label_map[cluster]
