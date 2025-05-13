# ml.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import os

def train_model(data_path="data/cleaned_data.csv", model_path="models/dropout_model.pkl"):
    print("[ML] Cargando datos procesados")
    df = pd.read_csv(data_path)

    X = df.drop(columns=["desercion"])
    y = df["desercion"]

    print("[ML] Dividiendo datos")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("[ML] Entrenando modelo")
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    print("[ML] Evaluando modelo")
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"[ML] Accuracy del modelo: {acc:.2f}")

    print(f"[ML] Guardando modelo en {model_path}")
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model()