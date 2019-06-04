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
data_comment = data.comment[0:100]
food_label = data.food[0:100]
drink_label = data.drink[0:100]
price_label = data.price[0:100]
staff_label = data.staff[0:100]
service_label = data.service[0:100]
space_label = data.space[0:100]
hygiene_label = data.hygiene[0:100]


######################### Build model
# chia tập train và test

# X_train,X_test,y_train,y_test = train_test_split(tfidf,food_label,test_size=0.3,random_state=10,shuffle=True)

svmClassifier = LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
        intercept_scaling=1, loss='squared_hinge', max_iter=100000,
        multi_class='ovr', penalty='l2', random_state=0, tol=1e-05, verbose=0)

stop_ws = (u'rằng',u'thì',u'là',u'mà','rang', 'thi', 'la', 'ma')
steps = []
steps.append(('CountVectorizer', CountVectorizer(ngram_range=(1,2),stop_words=stop_ws,max_df=0.5, min_df=1)))
steps.append(('tfidf', TfidfTransformer(use_idf=False, sublinear_tf = True,norm='l2',smooth_idf=True)))
steps.append(('classifier', svmClassifier))
clf = Pipeline(steps)
# clf.fit(data_comment, food_label)
# clf.fit(data_comment, drink_label)
# clf.fit(data_comment, price_label)
# clf.fit(data_comment, staff_label)
# clf.fit(data_comment, service_label)
# clf.fit(data_comment, space_label)
clf.fit(data_comment, hygiene_label)

# dump(clf, 'model_food.dat3') 
# dump(clf, 'model_drink.dat3') 
# dump(clf, 'model_price.dat3') 
# dump(clf, 'model_staff.dat3') 
# dump(clf, 'model_service.dat3') 
# dump(clf, 'model_space.dat3') 
dump(clf, 'model_hygiene.dat3') 

print('sucessful')