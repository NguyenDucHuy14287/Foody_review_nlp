import os

def run_cmd_build(model):
     path = os.getcwd()
     os.chdir(path + "/" + model)
     print("Build and dump " + model + ":")
     os.system("python3 build_model.py")
     print('\n')
     os.chdir(path)

def run_cmd_test(model):
     path = os.getcwd()
     os.chdir(path + "/" + model)
     print("Accuracy for " + model + ":")
     os.system("python3 test_model.py")
     print('\n')
     os.chdir(path)

def run_build_model(model_list):
     for i in range(len(model_list)):
          run_cmd_build(model_list[i])

def run_test_model(model_list):
     for i in range(len(model_list)):
          run_cmd_test(model_list[i])

def run():
     model_list = ["model_LR", "model_LR_CV", "model_NB", "model_SVM",
                     "model_SGD", "model_PAC", "model_RC"]
     run_build_model(model_list)
     run_test_model(model_list)

run()