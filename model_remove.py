import os 

def remove_data(model):
     path = os.getcwd()
     os.chdir(path + "/" + model)
     os.remove("train_data.csv")
     os.remove("test_data.csv")
     print("successful remove data " + model)
     os.chdir(path)

def remove_model(model):
     path = os.getcwd()
     os.chdir(path + "/" + model)
     os.remove("model_drink.dat3")
     os.remove("model_food.dat3")
     os.remove("model_staff.dat3")
     os.remove("model_space.dat3")
     os.remove("model_service.dat3")
     os.remove("model_price.dat3")
     os.remove("model_hygiene.dat3")
     print("successful remove model " + model)
     os.chdir(path)

def run_remove_data(list_model):
     for i in range(len(list_model)):
          remove_data(list_model[i])

def run_remove_model(list_model):
     for i in range(len(list_model)):
          remove_model(list_model[i])    

def run():
     model_list = ["model_LR", "model_LR_CV", "model_NB", "model_SVM",
                     "model_SGD", "model_PAC", "model_RC"]
     run_remove_data(model_list)
     run_remove_model(model_list)

run()