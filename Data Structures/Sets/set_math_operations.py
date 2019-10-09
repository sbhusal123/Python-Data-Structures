# intersection
s1 = {1,2,3,4}
s2 = {4,5,6}
s3 = {7,8,1,2,4}
intersection = s1 & s2 & s3
# print(intersection)

# union
fruit1 = {"apple","mango","guava"}
fruit2 = {"guava","pine-apple"}

fruits = fruit1 | fruit2
# print(fruits)

# symmetric difference
a = {1,2,3,4}
b = {5,6,3,4}
# print(a ^ b)

# difference
num = {0,1,2,3,4,5}
odd = {1,3,5}
even = num-odd
print(even)


# subset
fruits = {"apple","mango","banana","guava"}
fav = {"apple","guava"}
is_subset = fav <= fruits
# print(is_subset)

# superset
fruits = {"apple","mango","banana","guava"}
fav = {"apple","guava"}
is_superset = fruits >= fav
print(is_superset)


