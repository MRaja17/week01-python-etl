import pandas as pd
from pathlib import Path

def extract():
    return pd.read_csv("students.csv")

def transform(df):
    df = df.copy()

    # remove duplicate rows
    df = df.drop_duplicates()

    # clean column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # fill missing values
    df = df.fillna("")

    return df

def load(df):
    output = Path("output")
    output.mkdir(exist_ok=True)
    df.to_csv(output / "students_clean.csv", index=False)
    print("Saved: output/students_clean.csv")

def main():
    df = extract()
    df_clean = transform(df)
    load(df_clean)

if __name__ == "__main__":
    main()
