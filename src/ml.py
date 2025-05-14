import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def train_model():
    print("Entrenando modelo...")
    df = pd.read_csv("./processed/cleaned_data.csv")

    X = df.drop(columns=["desercion"])
    y = df["desercion"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Model Accuracy: {acc:.2f}")

    os.makedirs("./models", exist_ok=True)
    joblib.dump(model, "./models/dropout_model.pkl")
    print("Modelo guardado.")

if __name__ == "__main__":
    train_model()