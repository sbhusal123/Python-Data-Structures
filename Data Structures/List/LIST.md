#1. List
* General Purpose Data Structure.
* Most widely used.
* Size can be grown and shrinked as per the need.
* Can be sorted
* Sequence type (all basics operations covered in sequence operations supported)

## 1.1 Creating new List
* Using constructors, type casting, initializing with **[]** or list comprehension.

```python
"""initializing empty list using constructor""" 
x = list() 

"""initializing member of list by wrapping around []"""
y = ['a',25,'dog',123] 

"""by type-casting or conversion"""
tuple1 = (10,20)
z = list(tuple1)
```

**List Comprehension**

```python
a = [m for m in range(8)]
print(a) # [0,1,2,3,4,5,6,7]

b = [i**2 for i in range(10) if i>4]
print(b) # [25,36,48,64,81]
```

## 1.2 Deleting item in list
* Using **del(item)**
* Built-in function
 
```python
x = [7,2,3,4,1]
del(x[0])
print(x) # [2,3,4,5]

del(x)
print(x) # NameError: name 'x' is not defined
```
## 1.3 Adding item to the list
* *Syntax:* ``var_name.append(item)``
* Adds item to the tail of the list.

```python
x = [1,2,3,4]
x.append(5)
print(x) # [1, 2, 3, 4, 5]
```

## 1.3 Extending the list:
* Combining of two list
* Similar to adding of two list
* Adds new list to the tail of the list.
```python
x = [1,2,3,4,5]
y = [6,7,8,9,10]
x.extend(y)
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## 1.4 Inserting item to particular index
* *Syntax:* ``var_name.insert(index,item)``


```python
list1 = [5,3,8,6]
list2 = [9,10,11]
list1.insert(0,list2)
print(list1)
```

**Output:** ``[[9, 10, 11], 5, 3, 8, 6]``

**Note:** Here *list2* is inserted on the 0<sup>th</sup> index of *list1*.

```python
print(list1[0][2]) # accessing item in 0th index
```

**Output:** 11

## 1.5 Pop
* Pops last item off the list and returns item

```python
list1 = [7,6,5,[1,2,34]]

print(list1.pop()) # [1,2,34]
print(list1) # [7,6,5]
print(list1.pop()) # 5
print(list1) # [7,6]
```

## 1.6. Remove
* Removes first instance in the list.

```python
x = [3,3,6,6,7,8]

x.remove(6)
print(x) # [3,3,6,7,8]

x.remove(3) 
print(x) # # [3,6,7,8]
```

## 1.7. Reverse
* reverse the order of the list
* In place sort, **meaning:** It changes the original list.

```python
x = [5,3,8,6]
x.reverse()
print(x) # [6, 8, 3, 5]

y = [[1,2,3,4],7,6,8]
y.reverse()
print(y) # [8, 6, 7, [1, 2, 3, 4]]
```

## 1.8. Sorting (In place)
* **In place sorting.**
* Sorts the list in place.

```python
# inplace sorting
x = [5,2,8,5,1]
x.sort() 
print(x)

# sorting by creating new list
y = [5,2,8,5,1]
k = sorted(y)
print(k)
```

``Note: sorted(x) returns a new list without changing the original. 
While x.sort() puts the item of x in sorted order(in-place).``