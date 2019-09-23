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


@uppercase
def say_hi():
    return ['hello','this','is','surya']

# print(say_hi()) ['HELLO','THIS','IS','SURYA']


@splitText
def getText():
    return "This will be splitted into list"

# print(getText()) output: ['This', 'will', 'be', 'splitted', 'into', 'list']



