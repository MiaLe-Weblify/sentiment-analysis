import flask
from flask import Flask,render_template,url_for,request
import pandas as pd 
import joblib
import nltk
#per risolvere un bug, altrimenti da errore
nltk.download('punkt')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():

    classifier = joblib.load("ml-model.cls")
    
    if request.method == 'POST':
        def format_sentence(sent):
            return({word: True for word in nltk.word_tokenize(sent)})

        message = request.form['message']
        my_prediction = classifier.classify(format_sentence(message))
        
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 80, debug=True)