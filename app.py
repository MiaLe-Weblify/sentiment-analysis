import flask
from flask import Flask,render_template,url_for,request
import pandas as pd 
import joblib
import nltk
from flask_mysqldb import MySQL

#per risolvere un bug, altrimenti da errore
nltk.download('punkt')

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'minhanh0711'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

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
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyDB(message) VALUES (%s)", ([message]))
        mysql.connection.commit()
        cur.close()
        my_prediction = classifier.classify(format_sentence(message))
    return render_template('result.html',prediction = my_prediction)

@app.route('/opinion',methods=['GET', 'POST'])
def opinion(): 
    if request.method == 'POST': 
        req = request.form['options'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyDB(opinion) VALUES (%s)", ([req]))
        mysql.connection.commit()
        cur.close()
        print(req)
        return render_template('home.html')

    return render_template('opinion.html', opinion = req)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 80, debug=True)
