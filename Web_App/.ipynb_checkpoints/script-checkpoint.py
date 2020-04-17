#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import praw
import sys
import pandas as pd
import nltk
from nltk.stem import PorterStemmer    
from nltk.corpus import stopwords
import joblib
import re
from sklearn.preprocessing import LabelEncoder
from werkzeug.utils import secure_filename
from flask import jsonify



set(stopwords.words('english'))
ps = PorterStemmer() 
emoji_pattern = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       "]+", flags=re.UNICODE)

#creating instance of the class
app=Flask(__name__)
my_client_id = "tlaYd7tsDOqvlQ"
my_client_secret = "xdRqwLkA07r8ScyJZTMsYUndrSA"
my_user_agent = "scrapping r/india"
reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)
encoder = LabelEncoder()
encoder.classes_ = np.load('classes.npy',allow_pickle=True)

#prediction function
def FlarePredictor(link):
    link = link.split("comments")[1]
    post_id = link.split("/")[1]
    submission = reddit.submission(id=post_id)
    text = submission.title + " " + submission.selftext
    
    cleaned_text = np.array([text])
    cleaned_text = pd.Series(cleaned_text)
    cleaned_text = (cleaned_text.str.lower() #lowercase
                               .str.replace(r'[^\w\s]+', '') #rem punctuation 
                               .str.replace(emoji_pattern, '') #rem emoji
                               .str.replace(r'http\S+','') #rem links
                               .str.strip() #rem trailing whitespaces
                               .str.split()) #split by whitespaces
    res = []
    stop_words = set(stopwords.words('english')) 

    for i in cleaned_text:
        t = ""
        for j in i:
            if j not in stop_words:
                w = ps.stem(j)
                t += w
                t += " "
        res.append(t)
    cleaned_text = res

    vectorizer = joblib.load('tfidf.pickle')
    cleaned_text = vectorizer.transform(cleaned_text)
    model = joblib.load('model.pkl')
    prediction= model.predict(cleaned_text)
    return (encoder.inverse_transform(prediction))

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

#https://www.reddit.com/r/nextfuckinglevel/comments/g289tw/the_needle_galaxy_is_nearly_50_million_lightyears/

@app.route('/index',methods = ['POST'])
def result():
    link = request.form['text']
    flare = FlarePredictor(link)
    return render_template("index.html",prediction=flare)

#print(request, file=sys.stderr)
#if txt_file:
 #               filename = secure_filename(txt_file.filename)
  #              txt_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
   #             a = 'file uploaded'
    
@app.route('/automated_testing', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':
        for file in request.files:
            links = request.files[file].read()
            #Since a byte sized object is returned
            links = [links.decode('utf8').strip()]
            links = links[0].split("\n")
        
        res = dict()
        for i in links:
            f = FlarePredictor(i)
            res[i] = f[0]
        
        print(jsonify(res), file=sys.stderr)
       # return jsonify(res)
    else:
        return "GET REQ"
        
    return "Hi"
