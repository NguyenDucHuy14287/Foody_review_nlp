import pre_processing
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics import accuracy_score
import pandas as pd 

def test_model():
    model_food = load('model_food.dat3') 
    model_drink = load('model_drink.dat3') 
    model_price = load('model_price.dat3') 
    model_staff = load('model_staff.dat3') 
    model_service = load('model_service.dat3') 
    model_space = load('model_space.dat3') 
    model_hygiene = load('model_hygiene.dat3') 

    cont = True
    while (cont):
        content = input("Type comment here: ")
        content = pre_processing.string_preprocessing(content)
        food_label = model_food.predict([content])
        drink_label = model_drink.predict([content])
        price_label = model_price.predict([content])
        staff_label = model_staff.predict([content])
        service_label = model_service.predict([content])
        space_label = model_space.predict([content])
        hygiene_label = model_hygiene.predict([content])
        if (food_label==1):
            print("food, ")
        if (drink_label==1):
            print("drink, ")
        if (price_label==1):
            print("price, ")
        if (staff_label==1):
            print("staff, ")
        if (service_label==1):
            print("service, ")
        if (space_label==1):
            print("space, ")
        if (hygiene_label==1):
            print("hygiene, ") 
        if (input("Do you want to continue? ") == "no"):
            cont = False

def caculate_accuracy_single_label(X,true_label,model):
    predict_label = list(model.predict(X))
    accuracy = accuracy_score(true_label, predict_label) 
    return accuracy

def caculate_accuracy_multi_label(data,model_food,model_drink,model_price,
                        model_staff,model_service,model_space,model_hygiene):
    comment_var = list(data.comment)
    food_label = list(data.food)
    drink_label = list(data.drink)
    price_label = list(data.price)
    staff_label = list(data.staff)
    service_label = list(data.service)
    space_label = list(data.space)
    hygiene_label = list(data.hygiene)
    length = len(comment_var)

    predict_food_label = list(model_food.predict(comment_var))
    predict_drink_label = list(model_drink.predict(comment_var))
    predict_price_label = list(model_price.predict(comment_var))
    predict_staff_label = list(model_staff.predict(comment_var))
    predict_service_label = list(model_service.predict(comment_var))
    predict_space_label = list(model_space.predict(comment_var))
    predict_hygiene_label = list(model_hygiene.predict(comment_var))

    s = 0

    for i in range(length):
        if (predict_food_label[i] == food_label[i] and
            predict_drink_label[i] == drink_label[i] and
            predict_price_label[i] == price_label[i] and
            predict_staff_label[i] == staff_label[i] and
            predict_service_label[i] == service_label[i] and
            predict_space_label[i] == space_label[i] and
            predict_hygiene_label[i] == hygiene_label[i]):
            s = s + 1
    
    accuracy = s/length
    return accuracy

def test():
    data = pd.read_csv('test_data.csv',sep=',',keep_default_na=False)
    comment_var = list(data.comment)
    food_label = list(data.food)
    drink_label = list(data.drink)
    price_label = list(data.price)
    staff_label = list(data.staff)
    service_label = list(data.service)
    space_label = list(data.space)
    hygiene_label = list(data.hygiene)

    model_food = load('model_food.dat3') 
    model_drink = load('model_drink.dat3') 
    model_price = load('model_price.dat3') 
    model_staff = load('model_staff.dat3') 
    model_service = load('model_service.dat3') 
    model_space = load('model_space.dat3') 
    model_hygiene = load('model_hygiene.dat3') 

    accuracy_food   = caculate_accuracy_single_label(comment_var,food_label,model_food)
    accuracy_drink  = caculate_accuracy_single_label(comment_var,drink_label,model_drink)
    accuracy_price  = caculate_accuracy_single_label(comment_var,price_label,model_price)
    accuracy_staff  = caculate_accuracy_single_label(comment_var,staff_label,model_staff)
    accuracy_service = caculate_accuracy_single_label(comment_var,service_label,model_service)
    accuracy_space   = caculate_accuracy_single_label(comment_var,space_label,model_space)
    accuracy_hygiene = caculate_accuracy_single_label(comment_var,hygiene_label,model_hygiene)
    accuracy_all = caculate_accuracy_multi_label(data,model_food,model_drink,model_price,
                                    model_staff,model_service,model_space,model_hygiene)
    print("Accuracy for single Food label: " + str(accuracy_food))
    print("Accuracy for single Drink label: " + str(accuracy_drink))
    print("Accuracy for single Price label: " + str(accuracy_price))
    print("Accuracy for single Staff label: " + str(accuracy_staff))
    print("Accuracy for single Service label: " + str(accuracy_service))
    print("Accuracy for single Space label: " + str(accuracy_space))
    print("Accuracy for single Hygiene label: " + str(accuracy_hygiene))
    print("Accuracy for multi label: " + str(accuracy_all))

def run():
        test()

run()







