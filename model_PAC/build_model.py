import csv
import pandas as pd 
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from joblib import dump
from sklearn.pipeline import Pipeline

def build_model(model_num,data):
        #store value to a temporary variable
        data_comment = data.comment
        food_label = data.food
        drink_label = data.drink
        price_label = data.price
        staff_label = data.staff
        service_label = data.service
        space_label = data.space
        hygiene_label = data.hygiene


        ######################### Build model - Using SVM
        Classifier = PassiveAggressiveClassifier(C=1.0, average=False, class_weight=None,
              early_stopping=False, fit_intercept=True, loss='hinge',
              max_iter=1000, n_iter=None, n_iter_no_change=5, n_jobs=None,
              random_state=0, shuffle=True, tol=0.001,
              validation_fraction=0.1, verbose=0, warm_start=False)

        stop_ws = (u'rằng',u'thì',u'là',u'mà','rang', 'thi', 'la', 'ma')
        steps = []
        steps.append(('CountVectorizer', CountVectorizer(ngram_range=(1,2),stop_words=stop_ws,max_df=0.5, min_df=1)))
        steps.append(('tfidf', TfidfTransformer(use_idf=False, sublinear_tf = True,norm='l2',smooth_idf=True)))
        steps.append(('classifier', Classifier))
        model = Pipeline(steps)

        if (model_num==0):
                model.fit(data_comment, food_label)
                dump(model, 'model_food.dat3') 
                print('sucessful dump food model')
        elif (model_num==1):
                model.fit(data_comment, drink_label)
                dump(model, 'model_drink.dat3') 
                print('sucessful dump drink model')
        elif (model_num==2):
                model.fit(data_comment, price_label)
                dump(model, 'model_price.dat3') 
                print('sucessful dump price model')
        elif (model_num==3):
                model.fit(data_comment, staff_label)
                dump(model, 'model_staff.dat3') 
                print('sucessful dump staff model')
        elif (model_num==4):
                model.fit(data_comment, service_label)
                dump(model, 'model_service.dat3') 
                print('sucessful dump service model')
        elif (model_num==5):
                model.fit(data_comment, space_label)
                dump(model, 'model_space.dat3') 
                print('sucessful dump space model')
        elif (model_num==6):
                model.fit(data_comment, hygiene_label)
                dump(model, 'model_hygiene.dat3') 
                print('sucessful dump hygiene model')
        
def dump_model():
        ######################### read train data from csv file
        data = pd.read_csv('train_data.csv',sep=',',keep_default_na=False)

        for i in range(7):
                build_model(i,data)

def run():
        dump_model()

run()
