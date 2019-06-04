import pre_processing
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import pandas as pd 

clf = load('model.dat3') 

# comment = input("Enter comment: ")
content = pre_processing.string_preprocessing('mỗi lần nghĩ tới trò chơi trên bàn sẽ nghĩ tới vô đây được cái khoái món cơm chiên với cá viên trong đây lắm vô không kêu chơi hông vui cho anh đầu bếp ngàn like ạ hì hì')
y_pred = clf.predict([content])
print(y_pred)



