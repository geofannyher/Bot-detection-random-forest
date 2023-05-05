import numpy as np
from flask import Flask, request, render_template
import pickle
import joblib
import pandas as pd
# from analisis_data_profil import preprocess
app = Flask(__name__)

# model = pickle.load(open('models/model.pkl', 'rb'))
model = joblib.load('models/model.pkl')
# data = pd.read_csv('testing_dataset.csv')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
# def predict():
#     screen_name = request.form['screen_name']
#     user_data = data.loc[data['screen_name'] == screen_name]
    
#     if user_data.empty:
#         return render_template('index.html', error_message='screen_name tidak ditemukan')
    
#     features = user_data.drop('screen_name', axis=1)
#     prediction = model.predict(features)
    
#     if prediction[0] == 1:
#         result = 'Bot'
#     else:
#         result = 'Human'
    
#     return render_template('bot.html', screen_name=screen_name, prediction=result)

def predict():
    # Load data from CSV file
    data = pd.read_csv("testing_dataset.csv")

    # Get input values from HTML form
    input_features = [float(x) for x in request.form.values()]

    # Make prediction using Random Forest model
    prediction = model.predict([input_features])

    # Render prediction result to HTML template
    return render_template("index.html", prediction_text="Prediction: {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)