from pathlib import Path
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "etudiants.csv"
MODEL_FILE = BASE_DIR / "model.pkl"

def get_model():
    if MODEL_FILE.exists():
        return joblib.load(MODEL_FILE)
    data = pd.read_csv(DATA_FILE)
    X = data[["heures_revision", "exercices", "absence", "note_precedente"]]
    y = data["resultat"]
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    if os_writable(BASE_DIR):
        try:
            joblib.dump(model, MODEL_FILE)
        except Exception:
            pass
    return model

def os_writable(path):
    try:
        return path.exists() and path.is_dir() and bool(__import__("os").access(path, __import__("os").W_OK))
    except Exception:
        return False

def predict(heures_revision, exercices, absence, note_precedente):
    model = get_model()
    row = pd.DataFrame([{
        "heures_revision": heures_revision,
        "exercices": exercices,
        "absence": absence,
        "note_precedente": note_precedente,
    }])
    return int(model.predict(row)[0])
