import pandas as pd
import numpy as np
# Load dataset
dataset = pd.read_csv('testing_dataset.csv')
# dataset = pd.read_csv('training_dataset.csv')
# menghapus nilai duplikat yang sama
dataset = dataset.drop_duplicates(keep='first', inplace=False)
# mengubah format datetime dalam format standar
dataset['created_at']= pd.to_datetime(dataset['created_at'])
print(len(dataset))
print(dataset['created_at'].dtype)
# dataset.replace(np.inf, 0) 
# dataset.replace(-np.inf, 0)
dataset['ratio_statuses_count_per_age']=dataset['statuses_count']/dataset['account_age_days']
dataset['ratio_favorites_per_age']=dataset['favourites_count']/dataset['account_age_days']
dataset['ratio_friends_per_followers']=dataset['friends_count']/dataset['followers_count']
dataset['description'].fillna('x', inplace = True)
dataset['word_count']=dataset['description'].apply(lambda x: 
len(str(x).split(" ")))#count the word
dataset['char_count'] = dataset['description'].str.len() 
#count the character including space
dataset['reputation']= dataset['followers_count']/(dataset['followers_count']+ dataset['friends_count'])
dataset.head()
print(len(dataset))
#Feture Entrophy
# Mengubah tipe data kolom 'created_at' menjadi datetime
dataset['created_at'] = pd.to_datetime(dataset['created_at'])
#menugurutkan
dataset.sort_values(["screen_name", "created_at"])
dataset.head()
print(len(dataset))
dataset.drop(['created_at'], axis=1,inplace=True)
# dataset.head()
# mengubah menjadi boolean dan mengecek apakah tidak ada null.
dataset['location']=pd.notnull(dataset['location'])
dataset.head()
print(len(dataset))
# mengecek apakah dalam descripsi ada teks bot atau tidak dan menjadikannya kedalam bolean
import re
dataset['contains_bot_name']=dataset['description'].str.extract("\b(bot|b0t|updates|hourly|automatically|generating|generated|every|computer-generated|twitterbot|automated|FakeBots|')\b|Bots", 
                                                                    flags=re.IGNORECASE,expand=False)
                                                                    # regex=True)
dataset['contains_bot_name'].fillna(0).astype(bool).sum(axis=0)
#Feature avg_word
dataset['description'] = dataset['description'].astype(str)
dataset['description_word_count'] = dataset['description'].apply(lambda x: len(str(x).split()))
dataset['description_character_count'] = dataset['description'].apply(lambda x: sum(len(word) for word in str(x).split()))
dataset['avg_word'] = dataset['description_character_count'] / dataset['description_word_count']
dataset.head()
dataset.drop(['screen_name','description'], inplace=True, axis=1)
# dataset.head()
dataset.loc[:, ~dataset.columns.str.contains('^Unnamed:0')]
dataset["reputation"].fillna(0, inplace = True) 
dataset["contains_bot_name"].fillna(False, inplace=True)
dataset.replace(np.inf, 0)
dataset.replace(-np.inf, 0)
dataset=dataset.replace([np.inf, -np.inf], np.nan)
dataset=dataset.replace([np.inf, -np.inf], np.nan).dropna(how="all")
dataset = dataset.fillna(dataset.mean())

# dataset.to_csv('hasilpreprocessing_training.csv', index=False)
dataset.to_csv('hasilpreprocessing_testing.csv', index=False)

