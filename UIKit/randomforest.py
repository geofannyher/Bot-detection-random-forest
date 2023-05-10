import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score,accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from collections import OrderedDict
import joblib
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline

#data hasil preprocessing
data_baru = pd.read_csv("hasilpreprocessing_training.csv")

# #memilih feature yang akan digunakan kolom kecuali 'class'
X = data_baru.drop('account_type', axis=1)
# y kemudian digunakan sebagai target atau label dalam pemodelan
y = data_baru['account_type']

# membagi data menjadi training and testing sets untuk fitur X dan label y
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=42)

data_baru.head()
# Membuat model Random Forest Classifier menentukan 100 pohon keputusan yang akan dibangun 
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Melatih model dengan cara X_train berisi fitur atau atribut, sedangkan y_train data latih yang berisi label atau target yang sesuai dengan fitur-fitur tersebut.
model.fit(X_train, y_train)

tree_feature =  pd.Series(model.feature_importances_, X.columns).sort_values(ascending = True)
plt.figure(figsize = (8,8))
plt.barh(X.columns, tree_feature)
plt.xlabel('Feature Important Score', fontsize = 12)
plt.ylabel('Features', fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Visualizing Feature Importances', fontsize = 20)

# Menampilkan angka per fitur pada visualisasi
for i, v in enumerate(tree_feature):
    plt.text(v, i, str(round(v, 2)), color='black', va='center')

# memprediksi label atau target yang sesuai dengan fitur-fitur dalam X_test
y_pred = model.predict(X_test)

# Menghitung akurasi model pada dataset
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)

#menghitung confusion matrix berdasarkan label sebenarnya (y_test) dan hasil prediksi model (y_pred)
cm = confusion_matrix(y_test, y_pred)

# membuat plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
# print(cm)

print("Confusion Matrix:")
print("----------------------------------------")
print("True Positif (TP):", cm[1, 1])
print("False Positif (FP):", cm[0, 1])
print("True Negatif (TN):", cm[0, 0])
print("False Negatif (FN):", cm[1, 0])

# mencetak laporan klasifikasi
print(classification_report(y_test, y_pred))

#menyimpan model klasifikasi Random Forest dengan menggunakan pipeline
pipe = make_pipeline(MinMaxScaler(),RandomForestClassifier()) 

# melakukan pelatihan (fitting) model pada data pelatihan (X_train dan y_train).
pipe.fit(X_train, y_train)

#menyimpan model yang telah dilatih ke dalam file dengan ekstensi .pkl
joblib.dump(pipe, 'model.pkl')