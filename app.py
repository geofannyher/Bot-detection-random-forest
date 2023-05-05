# from flask import Flask, render_template, request
# import joblib
# import pandas as pd

# app = Flask(__name__)

# # Memuat model Random Forest Classifier
# model = joblib.load("model.pkl")

# # Memuat data test dari file CSV
# datatest = pd.read_csv("hasilpreprocessing.csv")

# @app.route("/")
# def home():
#     return render_template("bot.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     # Mengambil nilai input dari form HTML
#     input_values = [float(x) for x in request.form.values()]

#     # Membuat DataFrame dari nilai input
#     input_df = pd.DataFrame([input_values], columns=["favourites_count","avg_word", "followers_count", "friends_count","description_character_count","description_word_count","contains_bot_name","reputation","char_count","word_count","ratio_friends_per_followers","ratio_favorites_per_age","account_age_days","ratio_statuses_count_per_age","account_type", "screen_name","statuses_count","account_age_days","verified"])

#     # Memprediksi label menggunakan model
#     prediksi = model.predict(input_df)

#     # Menentukan pesan yang akan ditampilkan berdasarkan hasil prediksi
#     if prediksi[0] == 0:
#         message = "Bot"
#     else:
#         message = "Manusia"

#     return render_template("bot.html", prediction_text=message)

# @app.route("/batch_predict")
# def batch_predict():
#     # Memprediksi kelas untuk setiap data test
#     prediksi = model.predict(datatest)

#     # Menambah kolom "prediksi" ke dalam DataFrame datatest
#     datatest["prediksi"] = prediksi

#     # Menghitung jumlah bot dan manusia dalam data test
#     n_bot = (datatest["prediksi"] == 0).sum()
#     n_manusia = (datatest["prediksi"] == 1).sum()

#     # Menampilkan hasil jumlah bot dan manusia pada halaman web
#     return render_template("templatess/bot.html", n_bot=n_bot, n_manusia=n_manusia)

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Memuat model
model = joblib.load("models/model2.pkl")

# Memuat data testing
data_testing = pd.read_csv("hasilpreprocessing.csv")

# Membuat fungsi untuk melakukan prediksi
def prediksi():
    hasil_prediksi = []
    for i in range(len(data_testing)):
        fitur1 = data_testing.loc[i, "default_profile"]
        fitur2 = data_testing.loc[i, "favourites_count"]
        fitur3 = data_testing.loc[i, "followers_count"]
        fitur3 = data_testing.loc[i, "friends_count"]
        fitur4 = data_testing.loc[i, "location"]
        fitur5 = data_testing.loc[i, "statuses_count"]
        fitur6 = data_testing.loc[i, "verified"]
        fitur7 = data_testing.loc[i, "account_age_days"]
        fitur8 = data_testing.loc[i, "account_type"]
        
        fitur9 = data_testing.loc[i, "ratio_statuses_count_per_age"]
        fitur10 = data_testing.loc[i, "ratio_favorites_per_age"]
        fitur11 = data_testing.loc[i, "ratio_friends_per_followers"]
        fitur12 = data_testing.loc[i, "word_count"]
        fitur13 = data_testing.loc[i, "char_count"]
        fitur14 = data_testing.loc[i, "reputation"]
        fitur15 = data_testing.loc[i, "contains_bot_name"]
        fitur16 = data_testing.loc[i, "description_word_count"]
        fitur17 = data_testing.loc[i, "description_character_count"]
        fitur18 = data_testing.loc[i, "avg_word"]

        pred = model.predict([[fitur1, fitur2, fitur3,fitur4,fitur5,fitur6,fitur7,fitur8,fitur9,fitur10,fitur11,fitur12,fitur13,fitur14,fitur15,fitur16,fitur17,fitur18]])[0]
        hasil_prediksi.append({
            "data_ke": i+1,
            "fitur1": fitur1,
            "fitur2": fitur2,
            "fitur3": fitur3,
            "fitur4": fitur4,
            "fitur5": fitur5,
            "fitur6": fitur6,
            "fitur7": fitur7,
            "fitur8": fitur8,
            "fitur9": fitur9,
            "fitur10": fitur10,
            "fitur12": fitur12,
            "fitur13": fitur13,
            "fitur15": fitur15,
            "fitur16": fitur16,
            "fitur17": fitur17,
            "fitur18": fitur18,
            "hasil_prediksi": pred
        })
    return hasil_prediksi

# Membuat route untuk menampilkan hasil prediksi
@app.route("/")
def hasil():
    hasil_prediksi = prediksi()
    return render_template("cba.html", hasil_prediksi=hasil_prediksi)

if __name__ == "__main__":
    app.run(debug=True)
