#import library yang di butuhkan
import pandas as pd
import numpy as np
import re

# Load dataset
dataset = pd.read_csv('selected_data.csv')
# dataset = pd.read_csv('training_dataset.csv')

# menghapus nilai duplikat yang sama
dataset = dataset.drop_duplicates(keep='first', inplace=False)

# mengubah format datetime dalam format standar
dataset['created_at']= pd.to_datetime(dataset['created_at'])

# dataset.replace(np.inf, 0) 
# dataset.replace(-np.inf, 0)

#menghitung jumlah ratio status dengan engan membagi nilai kolom 'statuses_count' dengan nilai kolom 'account_age_days'
dataset['ratio_statuses_count_per_age']=dataset['statuses_count']/dataset['account_age_days']

#menghitung jumlah ratio status dengan engan membagi nilai kolom 'favourites_count' dengan nilai kolom 'account_age_days'
dataset['ratio_favorites_per_age']=dataset['favourites_count']/dataset['account_age_days']

#menghitung jumlah ratio status dengan engan membagi nilai kolom 'friends_count' dengan nilai kolom 'followers_count'
dataset['ratio_friends_per_followers']=dataset['friends_count']/dataset['followers_count']

#mengisi nilai yang hilang (missing values) dalam kolom 'description' dengan nilai 'x'.
dataset['description'].fillna('x', inplace = True)

# menghitung jumlah kata dalam kolom 'description' dan ambda ini akan mengubah nilai ke dalam string
dataset['word_count']=dataset['description'].apply(lambda x: 
len(str(x).split(" ")))#count the word

# menghitung jumlah karakter dalam setiap entri kolom 'description' dataset
dataset['char_count'] = dataset['description'].str.len()

#menghitung rasio reputasi dengan membagi jumlah pengikut dengan jumlah total pengikut dan teman
dataset['reputation']= dataset['followers_count']/(dataset['followers_count']+ dataset['friends_count'])
dataset.head()

# Mengubah tipe data kolom 'created_at' menjadi datetime
dataset['created_at'] = pd.to_datetime(dataset['created_at'])
#menugurutkan berdasarkan nama dan waktu
dataset.sort_values(["screen_name", "created_at"])
dataset.head()

#menghapus kolom created_at
dataset.drop(['created_at'], axis=1,inplace=True)
# dataset.head()

# mengubah menjadi boolean dan mengecek apakah tidak ada null.
dataset['location']=pd.notnull(dataset['location'])
dataset.head()

# mengecek apakah dalam descripsi ada teks bot atau tidak dan menjadikannya kedalam bolean
dataset['contains_bot_name']=dataset['description'].str.extract("\b(bot|b0t|updates|hourly|automatically|generating|generated|every|computer-generated|twitterbot|automated|FakeBots|')\b|Bots", 
                                                                    flags=re.IGNORECASE,expand=False)
                                                                    # regex=True)
#menghitung jumlah entri dalam kolom 'contains_bot_name' yang bernilai True.
dataset['contains_bot_name'].fillna(0).astype(bool).sum(axis=0)

#mengubah tipe data kolom 'description' menjadi tipe data string (str).
dataset['description'] = dataset['description'].astype(str)

#menghitung jumlah kata dalam setiap entri kolom 'description' dan menyimpan hasilnya dalam kolom baru 'description_word_count'
dataset['description_word_count'] = dataset['description'].apply(lambda x: len(str(x).split()))

 # menghitung jumlah karakter di setiap kata dalam kolom 'description',kemudian menjumlahkannya dan disimpan dalam kolom 'description_character_count'.
dataset['description_character_count'] = dataset['description'].apply(lambda x: sum(len(word) for word in str(x).split()))

# menghitung rata-rata jumlah karakter per kata di kolom 'description', dan disimpan dalam kolom 'avg_word'.
dataset['avg_word'] = dataset['description_character_count'] / dataset['description_word_count']
dataset.head()

#menghapus screen_name dan description
dataset.drop(['screen_name','description'], inplace=True, axis=1)
# dataset.head()
#memilih semua kolom dalam dataset kecuali kolom-kolom yang mengandung string "Unnamed:0"
dataset.loc[:, ~dataset.columns.str.contains('^Unnamed:0')]

# menggantikan nilai-nilai yang hilang dalam kolom 'reputation' dengan nilai 0
dataset["reputation"].fillna(0, inplace = True) 

# menggantikan nilai-nilai yang hilang dalam kolom 'contains_bot_name' dengan nilai False.
dataset["contains_bot_name"].fillna(False, inplace=True)

 # mengganti nilai tak terhingga (np.inf) dengan 0
dataset.replace(np.inf, 0)

# menggantikan nilai tak terhingga negatif (-np.inf)  dalam dataset dengan nilai 0.
dataset.replace(-np.inf, 0)

#menggantikan nilai tak terhingga (np.inf) dan nilai tak terhingga negatif (-np.inf) dalam dataset dengan nilai NaN (Not a Number)
dataset=dataset.replace([np.inf, -np.inf], np.nan)

# menggantikan nilai tak terhingga (np.inf) dan nilai tak terhingga negatif (-np.inf) dengan nilai NaN,kemudian menghapus baris yang seluruhnya terdiri dari nilai NaN
dataset=dataset.replace([np.inf, -np.inf], np.nan).dropna(how="all")
 # nilai-nilai yang hilang dalam dataset dengan nilai rata-rata dari setiap kolom
# dataset = dataset.fillna(dataset.mean())
numeric_columns = dataset.select_dtypes(include='number')
dataset[numeric_columns.columns] = dataset[numeric_columns.columns].fillna(dataset[numeric_columns.columns].mean())
# Menampilkan data dengan format yang lebih mudah dibaca
print(dataset.to_string(index=False))

dataset.to_csv('hasilpreprocessing_select.csv', index=False)
# dataset.to_csv('hasilpreprocessing_testing.csv', index=False)

