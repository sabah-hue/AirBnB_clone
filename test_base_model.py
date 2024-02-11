#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
m_json = my_model.to_dict()
print(m_json)
print("JSON of my_model:")
for key in m_json.keys():
    print("\t{}: ({}) - {}".format(key, type(m_json[key]), m_json[key]))
