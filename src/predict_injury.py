import numpy as np
from train_model import train_injury_prediction_model

def predict_injury_risk(model, new_data):
    return model.predict(new_data)

if __name__ == '__main__':
    model = train_injury_prediction_model()
    new_data = np.array([[/* new athlete data here */]])
    risk_prediction = predict_injury_risk(model, new_data)
    print('Injury Risk Prediction:', risk_prediction)
