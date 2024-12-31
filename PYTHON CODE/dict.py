dic = {"name": "Harshil", 
       "age": 20, 
       "city": "Bhavnagar"
}
print("Create a dictionary to store key-value pairs:", dic)
name = dic["name"]
print("Access dictionary elements using keys:", dic["name"])
age = dic["age"]
print("Access dictionary elements using keys:", dic["age"])
dic['age'] = 21
print("update dictionary elements using keys:", dic["age"])
del dic['city']
print("delete dictionary elements using keys:", dic)
keys = dic.keys()
values = dic.values()
items = dic.items()
print("Use dictionary methods like keys()", keys)
print("Use dictionary methods like values()", values)
print("Use dictionary methods like items()", items)
dic["country"] = "India"
print("Add a new key-value pair.", dic["country"])
dic.pop('name')
print("remove an existing key-value pair.", dic)
students = {
    'student1': {
        'name': 'Harnish',
        'age': 19,
        'marks': 90
    },
    'student2': {
        'name': 'Jay',
        'age': 18,
        "marks": 85
    }
}
print("Nested dictionary:", students)
student1_name = students['student1']['name']
student2_marks = students['student2']['marks']
print("Access nested dictionary elements:", student1_name, student2_marks)
students["student1"]["marks"] = 88
print("Update nested dictionary elements:", students["student1"]["marks"])
dict1 = {"a": 1, "b": 2}
print("dictionary 1:", dict1)
dict2 = {"b": 3, "c": 4}
print("dictionary 2:", dict2)
dict1.update(dict2)
print("Merge two dictionaries using update():", dict2)
unsorted_dict = {"apple": 3, "banana": 1, "cherry": 2}
print("Unsorted dictionary:", unsorted_dict)
sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
print("sorted dict:",sorted_dict)