import json


my_dict = {}

my_dict["nombre"] = "hengel"
my_dict["spellido"] = "beltre"

print(my_dict)
print(type(my_dict))

dict_json = json.dumps(my_dict)
print(type(dict_json))
print(dict_json)

