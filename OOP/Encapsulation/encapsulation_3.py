class Circle:
    def __init__(self, radius):
        self._radius = radius            # no validation - so you can enter bs
                                         # but even if there would be: it would only run once
    @property        
    def radius(self): # property decorator - so this method will be called like an attribute (Circle.radius)
        return self._radius

    @radius.setter # setter decorator - to add logic that runs every time radius attribute gets changed
    def radius(self, value):
        if value < 0:                                     # added validation
            raise ValueError("Radius cannot be negative") # if change of attribute is intended,
        self._radius = value                              # validation of argument will happen first.

    @property
    def diameter(self): # property decorator - so this method will be called like an attribute (Circle.diameter)
        return self._radius * 2

    @property
    def area(self): # property decorator - so this method will be called like an attribute (Circle.area)
        return 3.14159 * (self._radius ** 2)


c = Circle(1)    # correct input (but without validation vulnerable)
print(c.radius)
c.radius = -2    # wrong input   (validation caught it)
print(c.radius)

# show errors of values < 0
# show with validation in __init__ without setter, and without __init__ but with setter
## show once WITHOUT setter, and try to set the radius after instantiation (c.radius = 2)
## it is now read-only, but unchangeable