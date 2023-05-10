# # Memuat data yang ingin diuji
# import pandas as pd
# data = pd.read_csv("hasilpreprocessing_select.csv")


# # Memuat model Random Forest Classifier
# import joblib
# model = joblib.load("model.pkl")

# # Memprediksi label menggunakan model
# prediksi = model.predict(data.drop("account_type", axis=1))

# # Menghitung jumlah bot dan manusia dalam data
# jumlah_label_data = data["account_type"].value_counts()
# print("Jumlah bot dan manusia dalam data:")
# print(jumlah_label_data)

# # Menghitung jumlah bot dan manusia dalam hasil prediksi
# jumlah_prediksi = pd.Series(prediksi).value_counts()
# print("Jumlah bot dan manusia dalam hasil prediksi menggunakan model :")
# print(jumlah_prediksi)
import pandas as pd
import joblib

# Membaca dataset dari file CSV
df = pd.read_csv('hasilpreprocessing_select.csv')

# Memuat model Random Forest Classifier dari file pkl
model = joblib.load("model.pkl")

# Mengganti ID dengan nama pengguna pada hasil prediksi
def get_username(row):
    if row['id'] == 19923515:
        return 'geofany'
    elif row['id'] == 495716215:
        return 'adin'
    else:
        return ''

# Memprediksi label menggunakan model
prediksi = model.predict(df.drop("account_type", axis=1))

# Menggabungkan prediksi dengan dataset
df['Prediksi'] = prediksi
df['Username'] = df.apply(get_username, axis=1)

# # Menampilkan pesan berdasarkan label dan prediksi
# for index, row in df.iterrows():
#     if row['account_type'] == 'bot' and row['Prediksi'] == 'human':
#         print("Akun ini ternyata manusia")
#     elif row['account_type'] == 'human' and row['Prediksi'] == 'bot':
#         print("Akun ini ternyata bot")
# Menampilkan pesan berdasarkan label, prediksi, dan ID
for index, row in df.iterrows():
    if row['account_type'] == 'bot' and row['Prediksi'] == 'human':
        print("Akun ini manusia")
    elif row['account_type'] == 'human' and row['Prediksi'] == 'bot':
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
    elif row['id'] == 21758143:
        print("screen_name : MaverickSabre")
    elif row['id'] == 23330998:
        print("screen_name : hxhassan")
    elif row['id'] == 211550281:
        print("screen_name : giuliainnocenzi")
    elif row['id'] == 1015021614:
        print("screen_name : cordensmaureen")