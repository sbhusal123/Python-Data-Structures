def addFive(x):

    def addOne(x):
        return x +1

    def addTwo(y):
        return y+2

    def againAddTwo(z):
        return z+2

    return addOne(againAddTwo(addTwo(x)))

print(addFive(2))

