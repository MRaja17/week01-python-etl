import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

def load_data():
    # uses the file you just created in Intermediate 1
    df = pd.read_csv("output/students_clean.csv")
    return df

def pick_target(df):
    # pick a reasonable target column automatically
    candidates = ["passed", "pass", "target", "label", "result", "grade"]
    for c in df.columns:
        if c.lower() in candidates:
            return c
    # fallback: last column
    return df.columns[-1]

def main():
    df = load_data()

    target_col = pick_target(df)
    y = df[target_col].astype(str)

    X = df.drop(columns=[target_col])

    # split columns
    cat_cols = [c for c in X.columns if X[c].dtype == "object"]
    num_cols = [c for c in X.columns if c not in cat_cols]

    pre = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
            ("num", "passthrough", num_cols),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", pre),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)

    out = Path("output")
    out.mkdir(exist_ok=True)
    (out / "model_result.txt").write_text(
        f"Target column: {target_col}\nAccuracy: {acc:.4f}\n"
    )

    print("Saved: output/model_result.txt")
    print(f"Target column: {target_col} | Accuracy: {acc:.4f}")

if __name__ == "__main__":
    main()
