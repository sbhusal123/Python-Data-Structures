class CustomException(Exception):
  def __init__(self, message):
    super(CustomException, self).__init__(message)
    print(message)

class Person:
  """Our class to hold information about persons"""  

  def __init__(self, name, age, address):
    """
    Constctor to initialize person class
    """
    self.name = name
    self.age = age
    self.address = address
  

  def __is_available_attribute(self, attribute):
    """
    Check weather the attribute is available or not
    """
    if attribute not in self.__dict__:
      raise CustomException("Attribute Doesn't Exists")
    else:
      return True


  def update(self, attribute, value):
    """
    Update the instance attributes
    """
    try:
      is_availble_attrib = self.__is_available_attribute(attribute)
      if(is_availble_attrib):
        setattr(self, attribute, value)
    except CustomException:
      pass


person = Person("ram", 10, "Kalimati")
updated = person.update("asd", "ramesh")
print(person.__dict__["name"])

  
