# Tuples
* Immutable (can't add/change)
* Useul for fixed data
* Faster than list
* Type of sequence

## 1. Creating a new tuple:
* Usually initialized within **"()"** or with **","**
```python
x = () # initializing empty tuple
x = (1,2,3) # initializing within ()
x = 1,2,3 # initializing without ()
x = 2,  # the comma tells a python that it's a tuple


"""type casting"""
list1 = [1,2,3,4]
my_tuple = tuple(list1)
print(my_tuple) # (1,2,3,4)
```
**Note:** To define tuple with one item, you still need to put **","**.


## 2. Immutable property of tuple
* Tuples are immutable, **but member objects may be mutable.**

For example. If tuple contains any mutable data-structure then such member function
can be mutable.

**Immutable property of tuple**
```python
x = (1,2,3)
del(x[0])  # TypeError: 'tuple' object doesn't support item deletion
x[1] = 8 # TypeError: 'tuple' object does not support item assignment
```

**Mutable objects example**
```python
y = ([1,2,3],4,5) # tuple where first item is list
del(y[0][1]) # deleting 2 in list
print(y) # ([1, 3], 4, 5)


"""However two tuples can be concatenated"""
a = (1,2,3)
b = (4,5,6)
print(a+b) # (1, 2, 3, 4, 5, 6)
```

