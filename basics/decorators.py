def uppercase(function):
    '''
    :param function: function defined below the decorator
    '''
    def wraper():
        func = function() # output from function stored in variable
        make_uppercase = [x.upper() for x in func]
        return make_uppercase
    return wraper

def splitText(function):

    def wrapper():
        func = function()
        splitted = func.split()
        return splitted
    
    return wrapper


def listadd(function):
    def wrapper(k):
        x = function(k)
        y = sum(x)
        return y
    return wrapper

@listadd
def init_list(x):
    return x

# x = [1,2,3,4] 
# print(init_list(x)) # returns 10


@uppercase
def say_hi():
    return ['hello','this','is','surya']

# print(say_hi()) ['HELLO','THIS','IS','SURYA']


@splitText
def getText():
    return "This will be splitted into list"
# print(getText()) output: ['This', 'will', 'be', 'splitted', 'into', 'list']


"""Accessing value returned by decorator in decorated function"""
from functools import reduce

def decorator(func):
    def wrapper(*args, **kwargs):
        kwargs['sum'] = reduce(lambda x,y: x+y, args)
        return func(*args, **kwargs)
    return wrapper

@decorator
def foo(x=0, y=0, sum=None):
    # Here sum is returned by decorator
    print(x+y)
    return sum # 3

print(foo(2, 3))

"""
Output:
5
5
"""
