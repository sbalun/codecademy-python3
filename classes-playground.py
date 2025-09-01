#____________________________#
#      __main__ in Python    #
#____________________________#
# In Python, __main__ is an identifier used to reference the current file context.
# When a module is read from standard input, a script, or from an interactive prompt,
# its __name__ is set equal to __main__.
#
# Suppose we create an instance of a class called CoolClass.
# Printing the type() of the instance will result in:
#
# <class '__main__.CoolClass'>
#
# This means that the class CoolClass was defined in the current script file.
#____________________________#
# Instantiate Python Class
#____________________________#
 class Car:
#   "This is an empty class"
 ##  pass

# # Class Instantiation
ferrari = Car()

# In Python, a class needs to be instantiated before use.
#
# As an analogy, a class can be thought of as a blueprint (Car),
# and an instance is an actual implementation of the blueprint (Ferrari).
#____________________________#
#      Python repr method    #
#____________________________#
class Employee:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

john = Employee('John')
print(john) # John

# The Python __repr__() method is used to tell Python what the string representation of the class should be.
# It can only have one parameter, self, and it should return a string.
#____________________________#
#       Python class         #
#____________________________#
# Defining a class
class Animal:
  def __init__(self, name, number_of_legs):
    self.name = name
    self.number_of_legs = number_of_legs
# In Python, a class is a template for a data type. A class can be defined using the class keyword.
#____________________________#
#     Python init method     #
#____________________________#
class Animal:
  def __init__(self, voice):
    self.voice = voice

# When a class instance is created, the instance variable
# 'voice' is created and set to the input value.
cat = Animal('Meow')
print(cat.voice) # Output: Meow

dog = Animal('Woof')
print(dog.voice) # Output: Woof
# In Python, the .__init__() method is used to initialize a newly created object.
# It is called every time the class is instantiated.