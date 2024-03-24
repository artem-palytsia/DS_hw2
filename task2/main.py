from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://scmarrion2005:kosmonaft1035@cluster0.zkqznbf.mongodb.net/")

db = client.book



# Читання (Read)

# 1 Реалізуйте функцію для виведення всіх записів із колекції.

def all_items_in_db ():
    result = db.cats.find({})
    for el in result:
        print(el)       

# 2 Реалізуйте функцію, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.
        
def search_by_name(name):
    result = db.cats.find_one({"name": name})
    return result




# Оновлення (Update) 

# 1 Створіть функцію, яка дозволяє користувачеві оновити вік кота за ім'ям.

def update_age_by_name(name, age):
    return db.cats.update_one({"name": name}, {"$set": {"age": age}})

# 2 Створіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям.

def add_feature_by_name(name, feature):
    return db.cats.update_one({"name": name}, {"$push": {"features": feature}})




# Видалення (Delete)

# 1  Реалізуйте функцію для видалення запису з колекції за ім'ям тварини.

def delete_item_by_name(name):
    return db.cats.delete_one({"name": name})

# 2 Реалізуйте функцію для видалення всіх записів із колекції.

def delete_all_items():
    return db.cats.delete_many({})


