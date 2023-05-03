import numpy as np
from flask import Flask, request, render_template
import pickle
import joblib
import pandas as pd
# from analisis_data_profil import preprocess
app = Flask(__name__)

# model = pickle.load(open('models/model.pkl', 'rb'))
model = joblib.load('models/model.pkl')
data = pd.read_csv('testing_dataset.csv')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    screen_name = request.form['screen_name']
    user_data = data.loc[data['screen_name'] == screen_name]
    
    if user_data.empty:
        return render_template('index.html', error_message='screen_name tidak ditemukan')
    
    features = user_data.drop('screen_name', axis=1)
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        result = 'Bot'
    else:
        result = 'Human'
    
    return render_template('bot.html', screen_name=screen_name, prediction=result)

if __name__ == "__main__":
    app.run(debug=True)