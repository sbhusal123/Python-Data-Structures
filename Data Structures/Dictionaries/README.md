# Dictionaries
* Key/Values Pair.
* Associative array, like HashMap in java.
* Are unordered. i.e cannot be sorted.

## 1. Initializing Dictionary
```python
"""direct initialization using {key: value}"""
x = {'pork':25.53,'beef':33.8,'chicken':22.7}


"""type-casting: typecasting list containing tuples into dictionary"""
y = dict([('apple',120),('mango',80),('watermelon',50)])

"""initialization using constructor"""
z = dict(pork=25.53,beef=33.8) 
```

## 2. Adding / Updating item to the dictionary
* *Syntax:* ``var_name[key]=value``

```python
price = {'pork':500,'mutton':1200}
price["shrimp"] = 1200 # adding
print(price) # {'pork': 500, 'mutton': 1200, 'shrimp': 1200}
price["shrimp"] = 1300 # updating
print(price) # {'pork': 500, 'mutton': 1200, 'shrimp': 1300}
```
## 3. Length Of Items in dictionaries
```python
price = {'pork':500,'mutton':1200}
length = len(price)
print(length)
```
**Output:** ``2``

## 4. Delete all items from dictionary
```python
price = {'pork':500,'mutton':1200}
price.clear()
print(price) 
```
**Output:** ``{}``

## 5. Delete entire dictionary
```python
price = {'pork':500,'mutton':1200}
del(price)
```
**Ouput:** ``NameError: name 'price' is not defined.``

## 6. Accessing keys and values in a dictionary
* ``<dict_var>.keys()`` to access keys
* ``<dict_var>.items()`` to access items

```python
price = {'pork':500,'mutton':1200}
price_keys = price.keys()
price_values = price.values()

print(price_keys) # dict_keys(['pork', 'mutton'])
print(price_values) # dict_values([500, 1200])
```
**Note:** Results are stored in a list.

## 7. Checking membership in keys and values  
* Using keyword ``in``

### 7.1. Checking membership in keys    
```python
present = {'Steve Jobs':1,"Sundar Pichai":2,"Alan Turing":3} # name as key and roll as value
is_student_present = 'Steve Jobs' in present.keys()
print(is_student_present)
```

**Output:** ``True``

### 7.2. Checking membership in values    
```python
is_roll_present = 4 in present.values()
print(is_roll_present)
```

**Output:** ``False``

## 8. Iterating through items in dictionary
* Key,values are accessed using ``items()``

```python
x = {"a": 1, "b": 2}
for k, v in x.items(): # k,v are arbitrary variables
    print("{key} = {values}".format(key=k,values=v))
```

**Output:** ``a = 1 b = 2``

## 9. Dictionary keys as argument names to the function
```python
def foo(name, address):
    print('{n} lives at {a}'.format(n=name, a=address))

x = {'name': 'Ram',
     'address': 'Bhopal'
}

foo(**x)
```

**Output*:* ``Ram lives at Bhopal``

## 10. Merging two dictionaries

### a. Python 3.5+
```python
x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}

z = {**x, **y}

print(z)
```

### b. Python 2.x
```python
x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}

z = dict(x, **y)

```
**Output**: ``{'a': 1, 'b': 2, 'c': 3, 'd': 4}``

