import pandas as pd
from pathlib import Path

# ---------- EXTRACT ----------
def extract():
    data = [
        {"name": "Meghana", "age": "24", "city": "Arlington"},
        {"name": "Asha", "age": "", "city": "Dallas"},
        {"name": "John", "age": "31", "city": None},
    ]
    return pd.DataFrame(data)

# ---------- TRANSFORM ----------
def transform(df):
    df = df.copy()

    # fix age column
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["age"] = df["age"].fillna(df["age"].median())

    # fix city
    df["city"] = df["city"].fillna("Unknown")

    # new column
    df["age_group"] = df["age"].apply(
        lambda x: "young" if x < 30 else "adult"
    )

    return df

# ---------- LOAD ----------
def load(df):
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    df.to_csv(output_dir / "cleaned_data.csv", index=False)
    print("Data saved to output/cleaned_data.csv")

# ---------- RUN ETL ----------
def main():
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)

if __name__ == "__main__":
    main()
