class Shape: # Parent Class
    def __init__(self, name): # init with one name attribute as necessary init argument
        self.name = name

    def area(self): # instance method printing something
        print("Some generic shape area")

class Rectangle(Shape): # Child Class inheriting from Parent Class
    def __init__(self, name, width, height): # recreating init
        super().__init__(name) # taking name attribute from Parent Class
        self.width = width     # and adding two more arguments
        self.height = height

    def area(self): # same here: recreating the same instance method
        super().area() # taking parents method behavior and then
        print(f"The area of {self.name} is {self.width * self.height}") # adding some more behavior to it

my_rectangle = Rectangle("My Rectangle", 10, 5)
my_rectangle.area() # Output: "Some generic shape area\nThe area of My Rectangle is 50"