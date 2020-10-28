import flask
from flask import Flask,render_template,url_for,request
import pandas as pd 
import joblib
import nltk
import numpy as np

nltk.download('punkt')
app = Flask(__name__)

@app.route('/',methods=['POST'])
def predict():

    classifier = joblib.load("model-73acc.cls")

    def format_sentence(sent):
        return np.array([sent])

    data = request.get_json(force=True)
    message = str(data)
    prediction = classifier.predict(format_sentence(message))
    if prediction == 'pos': 
        ans = 'Positive'
    elif prediction == 'neg': 
        ans = 'Negative'
    elif prediction == 'neu': 
        ans = 'Neutral'
    output = {'results': ans}
    return output

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
