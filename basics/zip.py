numList = [19, 21, 46]
strList = ['one', 'two', 'three']
charList = ['@','&','*']

outputA = zip(numList, strList)
# print(list(outputA)) =  [(19, 'one'), (21, 'two'), (46, 'three')]

outputB = zip(strList, numList)
# print(list(outputB)) =   [('one', 19), ('two', 21), ('three', 46)]

outputC = zip(numList,strList,charList)
print(outputC)