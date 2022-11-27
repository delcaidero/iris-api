import joblib
import logging
import pandas as pd


logging.basicConfig(level=logging.INFO)


def load_model(model="model/iris_classifier.joblib"):
    """Grabs model from disk"""
    clf = joblib.load(model)
    return clf

def predict(values):
    """Takes values"""
    clf = load_model()
    prediction = clf.predict(values)
    logging.debug(f"Input values: {values}")
    logging.debug(f"Prediction: {prediction}")
    return prediction

def get_model_response(input):
    prediction = predict(input)
    prediction = int(prediction)
    if prediction == 0:
        label = "Setosa"
    elif prediction == 1:
        label = "versicolor"
    else:
        label = "virginica"
    return {
        'label': label,
        'prediction': int(prediction)
    }
