import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score,accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

data_baru = pd.read_csv("hasilpreprocessing_training.csv")
# #memilih feature yang akan digunakan
X = data_baru.drop('account_type', axis=1) # Memilih semua kolom kecuali 'class'
y = data_baru['account_type']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=42)
data_baru.head()
# Membuat model Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Melatih model dengan data latih
model.fit(X_train, y_train)

tree_feature =  pd.Series(model.feature_importances_, X.columns).sort_values(ascending = True)
plt.figure(figsize = (8,8))
plt.barh(X.columns, tree_feature)
plt.xlabel('Feature Important Score', fontsize = 12)
plt.ylabel('Features', fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Visualizing Feature Importances', fontsize = 20)
# Memprediksi label pada data uji
y_pred = model.predict(X_test)

# Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)
import matplotlib as mpl
import seaborn as sns
from matplotlib import pyplot as plt
from collections import OrderedDict

cm = confusion_matrix(y_test, y_pred)

# membuat plot confusion matrix
sns.heatmap(cm, annot=True, fmt='g')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
print(cm)
print(classification_report(y_test, y_pred))
#untuk menyimpan model
import joblib
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
pipe = make_pipeline(MinMaxScaler(),RandomForestClassifier()) 
pipe.fit(X_train, y_train)
joblib.dump(pipe, 'model.pkl')