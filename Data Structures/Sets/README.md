# Sets
* Stores non-duplicate items.
* Very fast access vs Lists.
* Supports math sets Operations(union, intersection)
* Are un-ordered.

 ## 1. Creating new sets
 ```python
 x = {1,2,3,4,4,4,4,4} # creating new set
print(x) # {1, 2, 3, 4}

y = set() # defining new empty set


list= [1,2,3,4,5]
set = set(list) # type-casting list into set
print(set)
 ``` 

## 2. Adding item to the set
```python
x = {1,1,2,2,3,3}
x.add(4)
print(x)
```
**Output:** ``{1, 2, 3, 4}``

## 3. Removing Item
```python
y = {"a","a","b","b","c","c"}
y.remove("a")
print(y)
```
**Output:** ``{'b', 'c'}``

## 4. Checking Membership
```python
fruits = {"apple","mango","banana","pineapple"}
check = "apple" in fruits
print(check)
```  
**Output:** ``True``

## 5. Cardinality/Length of set
```python
persons = {"ram","ram","shyam","shyam","hari"}
print(len(persons))
``` 
**Output:** ``3``

## 6. Pop items from set
* Pops out random item

```python
k = {"@",")","a","b"}
poped_item = k.pop()
print(poped_item)
``` 
**Output:** ``Varies because items are pooped out randomly.``

## 7. Delete items from the set
```python
temp = {"a","b","c","d"}
temp.clear()
print(temp)
```
**Output:** ``set()`` i.e empty or null set. 

## 8. Math set-operations
* Intersection(AND): ``set1 & set2``
* UNION(OR):``set1 | set2`` 
* Symmetric Difference(XOR) : ``set1 ^ set2``
* Difference (in set1 but not in set2): ``set1 - set2``
* Subset(set2 contains set1): ``set1 <= set2``
* Superset:(set1 contains set2): ``set1 >= set2``

### 8.1 Intersection
* Gives common elements in two or more the sets.
```python
s1 = {1,2,3,4}
s2 = {4,5,6}
s3 = {7,8,1,2,4}

intersection = s1 & s2 & s3
print(intersection)
```

**Output:** ``{4}``

### 8.2 Union:
* All the elements in two or more sets.
* **Operator:** ``|`` called pipe.
 
```python
fruit1 = {"apple","mango","guava"}
fruit2 = {"guava","pine-apple"}

fruits = fruit1 | fruit2
print(fruits)
```

**Output:** ``{'guava', 'apple', 'mango', 'pine-apple'}``

### 8.3 **Symmetric Difference(XOR)**
* New set is formed excluding common elements in both.
* **Operator:** ``^``
 
```python
a = {1,2,3,4}
b = {5,6,3,4}
print(a ^ b)
```

**Output:** ``{1, 2, 5, 6}
``

### 8.4. Difference
* Elements in first set but not in second.
* **Operator:** ``-``
```python
num = {0,1,2,3,4,5}
odd = {1,3,5}
even = num-odd
print(even)
```

**Output:** ``{0, 2, 4}``

### 8.5. Subset
* A set formed by taking few elements of another(parent) set.
* **Operator:** ``<=``

```python
fruits = {"apple","mango","banana","guava"}
fav = {"apple","guava"}
is_subset = fav <= fruits
print(is_subset)
```
**Output:** ``True`` 

### 8.6. Superset
* A parent set from which a second set is formed.
* Operator: ``>=`` i.e greater than or equal. 

```python
fruits = {"apple","mango","banana","guava"}
fav = {"apple","guava"}
is_superset = fruits >= fav
print(is_superset)
```
**Output:** ``True``


