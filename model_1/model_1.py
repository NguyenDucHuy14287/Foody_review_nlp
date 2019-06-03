import csv
import pandas as pd 
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from joblib import dump
from sklearn.pipeline import Pipeline
# from keras.models import Sequential
# from keras.layers.core import Dense

######################### đọc dữ liệu từ file csv
data = pd.read_csv('data.csv',sep=',',keep_default_na=False)

#lưu giá trị comment vào 1 biến tạm
data_comment = data.comment
food_label = data.food

#chia tập data train và data test
X_train,X_test,y_train,y_test = train_test_split(data_comment,food_label,test_size=0.3,random_state=10,shuffle=True)



# dump(clf, 'model.dat3') 

