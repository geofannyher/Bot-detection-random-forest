import pandas as pd
import joblib

# Membaca dataset dari file CSV
df = pd.read_csv('hasilpreprocessing_select.csv')

# Memuat model Random Forest Classifier dari file pkl
model = joblib.load("model.pkl")

# Memprediksi label menggunakan model
prediksi = model.predict(df.drop("account_type", axis=1))

# Menggabungkan prediksi dengan dataset
df['Prediksi'] = prediksi

# Menampilkan pesan berdasarkan label, prediksi, dan ID
for index, row in df.iterrows():
    if row['account_type'] == 'bot' and row['Prediksi'] == 'human':
        print("Akun ini manusia")
    elif row['account_type'] == 'human' and row['Prediksi'] == 'bot':
        print("Akun ini bot")
    elif row['account_type'] == 'human' and row['Prediksi'] == 'human':
        print("Akun ini human")
    elif row['account_type'] == 'bot' and row['Prediksi'] == 'bot':
        print("Akun ini bot")
    if row['id'] == 19923515:
        print("screen_name : abc_es")
    elif row['id'] == 495716215:
        print("screen_name : syakir_Metafora")
    elif row['id'] == 258478116:
        print("screen_name : ChangeYResults")
    elif row['id'] == 4469821522:
        print("screen_name : WeRaBot")
    elif row['id'] == 393483438:
        print("screen_name : ilbolly")
    elif row['id'] == 235667666:
        print("screen_name : AlexNunez_")
    elif row['id'] == 239085423:
        print("screen_name :AAstierOff")
    elif row['id'] == 4372811421:
        print("screen_name :engelsystem")
    elif row['id'] == 87828501:
        print("screen_name : nbswayne")
    elif row['id'] == 1015021614:
        print("screen_name : cordensmaureen")