class Employee:
    def __init__(self, name, position, salary):
        self.name = name  # Public attribute
        self._position = position  # PrOtEcTeD attribute
        self.__salary = salary  # PRIVATE attribute

    # Public method
    def display_info(self):
        print(f"Name: {self.name}, Position: {self._position}")
        self.__display_salary()  # PRIVATE method (but within public one, which is accessible)

    # PrOtEcTeD method
    def _change_position(self, new_position):
        self._position = new_position
        print(f"Position changed to {self._position}")

    # PRIVATE method
    def __display_salary(self):
        print(f"Salary: ${self.__salary}")

class Manager(Employee):
    def promote_employee(self, employee):
        employee._change_position("Super " + employee._position)

employee = Employee("Alice", "Developer", 80000)
manager  = Manager("Bob", "Manager", 100000)

employee.display_info()

employee._change_position("Senior "+ employee._position) # using the protected method from outside - a no-no!
manager.promote_employee(employee) # using the protected method via a public method - that's what's up.
#employee.__display_salary() # won't work
employee._Employee__display_salary() # works, but how could you man godamn

employee.display_info()