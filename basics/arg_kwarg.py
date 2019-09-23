def addMany(*arg):
    # allows as many parameters to be passed
    sum = 0
    for item in arg:
        sum = sum + item
    return sum

def keyValuePairing(**kwargs):
    # allows passing of multiple key value paired argument
    for key,value in kwargs.items():
        print("{} = {}".format(key,value))

keyValuePairing(fname="surya",lname="bhusal",email="suya@asd.asd")




