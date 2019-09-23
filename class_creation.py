class Employee:

    def __init__(self,name,position):
        self.name= name
        self.position = position

    @classmethod
    def getName():
        return "Hello this is me"



e = Employee()
e.getName()
