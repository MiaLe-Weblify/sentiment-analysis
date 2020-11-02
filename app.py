import flask
from flask import Flask,render_template,url_for,request
import pandas as pd 
import joblib
import nltk
import numpy as np
import os 

nltk.download('punkt')
app = Flask(__name__)

@app.route('/',methods=['POST'])
def predict():
    filename = os.path.join(app.config['APP_PATH'], 'model-73acc.cls')
    with open(filename, 'rb') as f:
        classifier = joblib.load(f)

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
