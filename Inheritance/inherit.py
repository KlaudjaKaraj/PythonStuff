class Vehicle: # PARENT CLASS
    def __init__(self, brand, year): # initial init of Parent Class (Vehicle)
        self.brand = brand
        self.year = year

    def start(self):
        print("Starting the vehicle...") # start method of Parent Class (Vehicle)

class Car(Vehicle): # CHILD CLASS
    def __init__(self, brand, year, model): # recreate init so parent init is overwritten
        super().__init__(brand, year)       # but wants to keep part of parent init attributes
        self.model = model

    def start(self): # recreate start method
        super().start() # but want to have parent class start method
        print(f"{self.brand} {self.model} is now running.") # plus some extra behavior

class ElectricCar(Car): # (grand)CHILD CLASS
    def __init__(self, brand, year, model, battery_size): # recreate init so parent init is overwritten
        super().__init__(brand, year, model) # getting parent class init attributes 
        self.battery_size = battery_size # adding another attribute

    def start(self): # recreating start method (again)
        super().start() # but want to have parent class start method
        print(f"Electric engine is now on. Battery size: {self.battery_size} kWh.") # adding extra behavior

my_electric_car = ElectricCar("Tesla", 2022, "Model S", 75)
my_electric_car.start() # Output: "Starting the vehicle... Tesla Model S is now running. Electric engine is now on. Battery size: 75 kWh."