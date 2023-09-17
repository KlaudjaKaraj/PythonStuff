# In Python, class variables and instance variables are used to store data within a class, 
#but they have different scopes and behaviors.

# 1. Class Variables:
# Class variables are shared among all instances of a class. 
# They belong to the class itself rather than any specific instance. 
# You define a class variable within the class, outside of any methods. 
# Class variables are typically used to store data that is common to all instances of the class. 


# In this example, class_variable is a class variable.
class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Instance Variables:
# Instance variables are unique to each instance of a class. 
# They are defined within methods of the class and are prefixed with self. to bind them to a particular instance. 
# Each instance can have its own values for these variables.


# In this example, instance_variable is an instance variable specific to each instance of the class.
class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

