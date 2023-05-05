# Memuat data yang ingin diuji
import pandas as pd
data = pd.read_csv("hasilpreprocessing_testing.csv")

# Memuat model Random Forest Classifier
import joblib
model = joblib.load("model.pkl")

# Memprediksi label menggunakan model
prediksi = model.predict(data.drop("account_type", axis=1))

# Menghitung jumlah bot dan manusia dalam data
jumlah_label_data = data["account_type"].value_counts()
print("Jumlah bot dan manusia dalam data:")
print(jumlah_label_data)

# Menghitung jumlah bot dan manusia dalam hasil prediksi
jumlah_prediksi = pd.Series(prediksi).value_counts()
print("Jumlah bot dan manusia dalam hasil prediksi menggunakan model :")
print(jumlah_prediksi)
