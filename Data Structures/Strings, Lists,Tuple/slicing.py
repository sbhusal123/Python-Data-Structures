# slicing  of string
x = "computer"
"""
c -> 0 -> -8
o -> 1 -> -7
m -> 2 -> -6
p -> 3 -> -5
u -> 4 -> -4
t -> 5 -> -3
e -> 6 -> -2
r -> 7 -> -1
"""

"""from 1st index to 3rd index."""
print(x[1:4])  # omp

"""from 1st index to 5th index with step of 2."""
print(x[1:6:2])  # opt

"""From 3rd index to last index."""
print(x[3:])  # puter

"""Last element indexing."""
print(x[-1])  # r

"""third last to last index."""
print(x[-3:])  # ter

"""from first index to third last."""
print(x[:-2])  # comput

"""Accessing last element from right."""
print(x[-8])  # c

# slicing of tuples
