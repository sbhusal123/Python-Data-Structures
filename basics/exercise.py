x1 = [1,2,3,4,5]
x2 = [6,7,8,9,10]

x3 = [x+y for x,y in zip(x1,x2)]
print(x3)