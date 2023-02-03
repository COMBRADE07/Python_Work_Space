# Dictionaries:
"""
    methods of dictionary

    my_dict = { key1:value1, key2:value2, key3:value3, key4:value4 }

    my_dict.keys()              --- returns all keys of dictionary
    my_dict.values()            --- returns all values of dictionary
    my_dict.update({key:value}) --- update dictionary with new value
        ~~ note:    if key doesn't exist then it will create new key and
                    add key value to dictionary
    my_dict.clear()             --- clear all dictionary
    my_dict.pop()               --- remove last element(key-value) from dict.

    var = my_dict.items()       --- return each item in dictionary as tuple
    mydict['key'] = newValue    --- update key value with newValue
    mydict['newKey'] = newValue --- add new element in dictionary
    mydict['key']               --- access value store at mention key


     ~ create dictionary using  constructor
      ==> dict_name = dict(key = value,.......)

"""
my = {"Name": "Rhutik", "Address": "Pune", "HomeTown": "Akole"}

# create dictionary using method dict()

okay = dict(Name="Rhutik", College="DYP", Year="2022")
print(okay)

print(my.keys())
print(my.values())
my.pop("Address")
print(my)
print(my.get("HomeTown"))
print(type(my))
print(my["Name"])

# adding new key and value  and Update old value to dictionary

my['contact'] = 1234567890  # adding new value to dictionary
my['Name'] = "Hritik"  # update Rhutik as Hritik

print(my)

# nested dictionary
children_data = {
    "Child1": {
        "name": "C1",
        "Age": "12",
    },
    "Child2": {
        "name": "C2",
        "Age": "13",
    },
    "Child3": {
        "name": "C3",
        "Age": "11",
    },
    "Child4": {
        "name": "C4",
        "Age": "13",
    }
}
print()
print(children_data["Child1"]["name"])  # accessing child1 name in nested dictionary
print(children_data)

list_dict = [
    {"q": "What is your name?", "a": "True"},
    {"q": "What is your Age?", "a": "False"}
]

# print(type(list_dict))
# i = 1
# for data in list_dict:
#     ques = data['q']
#     ans = data['a']
#     print(f"Q.{i}] {ques}\t answer:{ans} ")
#     i += 1

ldata = list_dict.copy()
class happy:
    def __init__(self, list_dict):
        self.list_dict = list_dict

    def printx(self):
        i1 = 1
        print("From printx")
        for i in list_dict:
            q1 = i['q']
            a1 = i['a']
            print(f"Q.{i1}] {q1}\t answer:{a1} ")
            i1 += 1


obj = happy(ldata)
obj.printx()
# from Demo_Dictionary import demo_d as d
#
# Brand = d['brand']
# Model = d['model']
# Year = d['year']
# print(d.keys())
#
# print(f"Car brand is {Brand} and model {Model} is launched at {Year}.")
