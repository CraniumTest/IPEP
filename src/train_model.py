import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from utils import load_athlete_data, preprocess_data

def train_injury_prediction_model():
    df = load_athlete_data('data/sample_athlete_data.csv')
    df = preprocess_data(df)

    X = df.drop('injury', axis=1)
    y = df['injury']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')

    return model

if __name__ == '__main__':
    train_injury_prediction_model()
