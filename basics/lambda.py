'''
While normal functions are defined using the def keyword, in Python
anonymous functions are defined using the lambda keyword.
'''

addTwo = lambda x: x+2
# addTwo(5) output = 7

addTwoInlist = lambda x: [y+2 for y in x]
# addTwoInlist([1,2,3,4]) output = [3,4,5,6]

mylist = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0,mylist))
# print(even) = [2,4,6]


names = ['surya','mahima','ramesh','suman','sriya']
names_starting_with_su = list(filter(lambda x: list(x)[0]=='s' and list(x)[1] =='u',names))
# print(names_starting_with_su) = ['surya','suman']