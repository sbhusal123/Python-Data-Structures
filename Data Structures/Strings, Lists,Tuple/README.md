# 1. Indexing:
* Accessing any item in sequence using it's index.
* Starts with 0 for the first item. So **fourth element is 3 i.e [4-1]**
* Can be accessed using square bracket **[index_numer]**

For example. Consider the following example:

## 1.1 Indexing String
```python

# String 
x = "surya"
print(x[3]) # output = y
``` 

## 1.2 Indexing List
```python

# list
x = ['surya','ramesh','kiran']
print(x[1]) # output = ramesh

```        

## 1.3 Indexing Tuples
```python
#tuple
x = ('surya','ramesh','kiran')
print(x[1]) # output = ramesh
```

# 2.Slicing
* Slices out substring, substring, subtuples, using indexes.
* *Syntax* : [start:end+1:step]. Mathematical equivalence of indexing: [start,end)    

## 2.1 Slicing Of String:
```python
# indexing of string
x = "computer"
```
**Index provided:**

| Letter   |      From Left     |  From Right |
|----------|:------------------:|------------:|
|   c      |      0             |    -8       |
|   o      |      1             |    -7       |
|   m      |      2             |    -6       |
|   p      |      3             |    -5       |
|   u      |      4             |    -4       |
|   t      |      5             |    -3       |
|   e      |      6             |    -2       |
|   r      |      7             |    -1       |


``` python

"""from 1st index to 3rd index"""
print(x[1:4])  # omp
```

```python
"""from 1st index to 5th index with step of 2"""
print(x[1:6:2])  # opt
```

```python
"""From 3rd index to last index"""
print(x[3:])  # puter
```

```python
"""Last element indexing"""
print(x[-1])  # r
```

```python
"""third last to last index"""
print(x[-3:])  # ter
```

```python
"""from first index to third last"""
print(x[:-2]) # comput
```

```python
print(x[-8]) # c
``` 