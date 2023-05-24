#import library yang di butuhkan
import pandas as pd
import numpy as np
import re

# Load dataset2
dataset = pd.read_csv('selected_data.csv')
# dataset2 = pd.read_csv('training_dataset2.csv')

# menghapus nilai duplikat yang sama
dataset2 = dataset.drop_duplicates(keep='first', inplace=False)

# mengubah format datetime dalam format standar
dataset2['created_at']= pd.to_datetime(dataset2['created_at'])

# dataset2.replace(np.inf, 0) 
# dataset2.replace(-np.inf, 0)

#menghitung jumlah ratio status dengan engan membagi nilai kolom 'statuses_count' dengan nilai kolom 'account_age_days'
dataset2['ratio_statuses_count_per_age']=dataset2['statuses_count']/dataset2['account_age_days']

#menghitung jumlah ratio status dengan engan membagi nilai kolom 'favourites_count' dengan nilai kolom 'account_age_days'
dataset2['ratio_favorites_per_age']=dataset2['favourites_count']/dataset2['account_age_days']

#menghitung jumlah ratio status dengan engan membagi nilai kolom 'friends_count' dengan nilai kolom 'followers_count'
dataset2['ratio_friends_per_followers']=dataset2['friends_count']/dataset2['followers_count']

#mengisi nilai yang hilang (missing values) dalam kolom 'description' dengan nilai 'x'.
dataset2['description'].fillna('x', inplace = True)

# menghitung jumlah kata dalam kolom 'description' dan ambda ini akan mengubah nilai ke dalam string
dataset2['word_count']=dataset2['description'].apply(lambda x: 
len(str(x).split(" ")))#count the word

# menghitung jumlah karakter dalam setiap entri kolom 'description' dataset2
dataset2['char_count'] = dataset2['description'].str.len()

#menghitung rasio reputasi dengan membagi jumlah pengikut dengan jumlah total pengikut dan teman
dataset2['reputation']= dataset2['followers_count']/(dataset2['followers_count']+ dataset2['friends_count'])
dataset2.head()

# Mengubah tipe data kolom 'created_at' menjadi datetime
dataset2['created_at'] = pd.to_datetime(dataset2['created_at'])
#menugurutkan berdasarkan nama dan waktu
dataset2.sort_values(["screen_name", "created_at"])
dataset2.head()

#menghapus kolom created_at
dataset2.drop(['created_at'], axis=1,inplace=True)
# dataset2.head()

# mengubah menjadi boolean dan mengecek apakah tidak ada null.
dataset2['location']=pd.notnull(dataset2['location'])
dataset2.head()

# mengecek apakah dalam descripsi ada teks bot atau tidak dan menjadikannya kedalam bolean
dataset2['contains_bot_name']=dataset2['description'].str.extract("\b(bot|b0t|updates|hourly|automatically|generating|generated|every|computer-generated|twitterbot|automated|FakeBots|')\b|Bots", 
                                                                    flags=re.IGNORECASE,expand=False)
                                                                    # regex=True)
#menghitung jumlah entri dalam kolom 'contains_bot_name' yang bernilai True.
dataset2['contains_bot_name'].fillna(0).astype(bool).sum(axis=0)

#mengubah tipe data kolom 'description' menjadi tipe data string (str).
dataset2['description'] = dataset2['description'].astype(str)

#menghitung jumlah kata dalam setiap entri kolom 'description' dan menyimpan hasilnya dalam kolom baru 'description_word_count'
dataset2['description_word_count'] = dataset2['description'].apply(lambda x: len(str(x).split()))

 # menghitung jumlah karakter di setiap kata dalam kolom 'description',kemudian menjumlahkannya dan disimpan dalam kolom 'description_character_count'.
dataset2['description_character_count'] = dataset2['description'].apply(lambda x: sum(len(word) for word in str(x).split()))

# menghitung rata-rata jumlah karakter per kata di kolom 'description', dan disimpan dalam kolom 'avg_word'.
dataset2['avg_word'] = dataset2['description_character_count'] / dataset2['description_word_count']
dataset2.head()

#menghapus screen_name dan description
dataset2.drop(['screen_name','description'], inplace=True, axis=1)
# dataset2.head()
#memilih semua kolom dalam dataset2 kecuali kolom-kolom yang mengandung string "Unnamed:0"
dataset2.loc[:, ~dataset2.columns.str.contains('^Unnamed:0')]

# menggantikan nilai-nilai yang hilang dalam kolom 'reputation' dengan nilai 0
dataset2["reputation"].fillna(0, inplace = True) 

# menggantikan nilai-nilai yang hilang dalam kolom 'contains_bot_name' dengan nilai False.
dataset2["contains_bot_name"].fillna(False, inplace=True)

 # mengganti nilai tak terhingga (np.inf) dengan 0
dataset2.replace(np.inf, 0)

# menggantikan nilai tak terhingga negatif (-np.inf)  dalam dataset2 dengan nilai 0.
dataset2.replace(-np.inf, 0)

#menggantikan nilai tak terhingga (np.inf) dan nilai tak terhingga negatif (-np.inf) dalam dataset2 dengan nilai NaN (Not a Number)
dataset2=dataset2.replace([np.inf, -np.inf], np.nan)

# menggantikan nilai tak terhingga (np.inf) dan nilai tak terhingga negatif (-np.inf) dengan nilai NaN,kemudian menghapus baris yang seluruhnya terdiri dari nilai NaN
dataset2=dataset2.replace([np.inf, -np.inf], np.nan).dropna(how="all")
 # nilai-nilai yang hilang dalam dataset2 dengan nilai rata-rata dari setiap kolom
# dataset2 = dataset2.fillna(dataset2.mean())
numeric_columns = dataset2.select_dtypes(include='number')
dataset2[numeric_columns.columns] = dataset2[numeric_columns.columns].fillna(dataset2[numeric_columns.columns].mean())
# Menampilkan data dengan format yang lebih mudah dibaca
# print(dataset2.to_string(index=False))

import json
print("Data sebelum di Preprocessing")
# Mengubah DataFrame menjadi struktur JSON
json_data = {'data': dataset.to_dict(orient='records')}

# Mengkonversi menjadi JSON string
json_str = json.dumps(json_data, indent=2)

# Menampilkan JSON string
print(json_str)
print("Data sesudah di Preprocessing")
# Mengubah DataFrame menjadi struktur JSON
json_data = {'data': dataset2.to_dict(orient='records')}

# Mengkonversi menjadi JSON string
json_str = json.dumps(json_data, indent=2)

# Menampilkan JSON string
print(json_str)

dataset2.to_csv('hasilpreprocessing_select.csv', index=False)
# dataset2.to_csv('hasilpreprocessing_testing.csv', index=False)

