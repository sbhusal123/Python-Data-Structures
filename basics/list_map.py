x1 = [1,2,3,4,5]
x2 = [6,7,8,9,10]


# must typecast into list because initial parameters are also list
x3 = list(map(lambda n1,n2: n1+n2,x1,x2))
# print(x3) [7,9,11,13,15]



def addTwo(x):
    return x+2

x4 = list(map(addTwo,x1))

# print(x4) [3,4,5,6,7]


def stringSplit(x):
    return x.split(" ")

myStrinng = ['Test string 1', 'Test String 2','Test String 3']
splitted = list(map(stringSplit,myStrinng))
# print(splitted) 
# output: [['Test', 'string', '1'], ['Test', 'String', '2'], ['Test', 'String', '3']]

x3 = [x+y for x,y in zip(x1,x2)]
print(x3)