import pandas as pd
from pandas import DataFrame
import csv
from sklearn.model_selection import train_test_split
import pre_processing

#process and export data
def handle_data(data,export_add):
     # convert to list
     comment_var = list(data.comment)

     #export csv to each column
     id_var = list(data.id)
     comment_var1 = pre_processing.data_preprocessing(comment_var)
     food_var = list(data.food)
     drink_var = list(data.drink)
     price_var = list(data.price)
     staff_var = list(data.staff)
     service_var = list(data.service)
     space_var = list(data.space)
     hygiene_var = list(data.hygiene)

     cleaned_data = {'id': id_var,
          'comment': comment_var1,
          'food': food_var,
          'drink': drink_var,
          'price': price_var,
          'staff': staff_var,
          'service': service_var,
          'space': space_var,
          'hygiene': hygiene_var,
          }

     df = DataFrame(cleaned_data, columns= ['id', 'comment','food','drink','price','staff','service','space','hygiene'])
     export_csv = df.to_csv (export_add, index = None, header=True)

def export_data(model_list):
     #read raw data from csv file
     raw_data = pd.read_csv('data/data.csv',sep=',',keep_default_na=False)

     #spit data into train and test dataset 
     train_set, test_set = train_test_split(raw_data, test_size=0.3,shuffle=True)

     #pre-processing and dum data to csv
     for i in range(len(model_list)):
          handle_data(train_set,model_list[i] + "/train_data.csv")
          handle_data(test_set,model_list[i]  + "/test_data.csv")
     
     print("successful export data")

def run():
     model_list = ["model_LR", "model_LR_CV", "model_NB", "model_SVM",
                     "model_SGD", "model_PAC", "model_RC"]
     export_data(model_list)

run()