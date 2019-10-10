# Adding item to the dictionary
price = {'pork' : 500, 'mutton' : 1200}
price["shrimp"] = 1200 # adding
# print(price) # {'pork': 500, 'mutton': 1200, 'shrimp': 1200}
price["shrimp"] = 1300 # updating
# print(price) # {'pork': 500, 'mutton': 1200, 'shrimp': 1300}

# length pf items in dictionary
price = {'pork': 500, 'mutton': 1200}
length = len(price)
# print(length) # 2

# deleting all the items from dictionary
price = {'pork': 500, 'mutton': 1200}
price.clear()
# print(price) # {}

# deleting entire dictionary
price = {'pork': 500, 'mutton': 1200}
del price
# print(price)

# accessing key,values in dictionary
price = {'pork': 500,'mutton': 1200}
price_keys = price.keys()
price_values = price.values()
print(price_keys)
print(price_values)


# checking membership in keys and values
present = {'Steve Jobs': 1, "Sundar Pichai": 2,"Alan Turing": 3}  # name as key and roll as value

is_student_present = 'Steve Jobs' in present.keys()
print(is_student_present)

is_roll_present = 4 in present.values()
print(is_roll_present)

# Iterating through items in dictionary
x = {"a": 1, "b": 2}
for k, v in x.items():
    print("{key} = {values}".format(key=k,values=v))
