x = [1,2,3,4,5]
del(x[0])
print(x)  # [2,3,4,5]

del(x)
print(x) # NameError: name 'x' is not defined