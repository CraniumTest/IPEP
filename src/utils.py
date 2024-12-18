import pandas as pd

def load_athlete_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Implement necessary preprocessing such as handling missing values, encoding categorical data, etc.
    df.fillna(df.mean(), inplace=True)
    return df
