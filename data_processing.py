import pandas as pd
from pandas import DataFrame
import csv
from sklearn.model_selection import train_test_split
import pre_processing

#process and export data
def process_data(data,export_add):
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

def handle_data():
    #read raw data from csv file
    raw_data = pd.read_csv('data_first100.csv',sep=',',keep_default_na=False)

    #spit data into train and test dataset 
    train_set, test_set = train_test_split(raw_data, test_size=0.2,shuffle=True)

    #pre-processing and dum data to csv
    process_data(train_set,"model_2\\train_data.csv")
    process_data(test_set,"model_2\\test_data.csv")

    print("successful")