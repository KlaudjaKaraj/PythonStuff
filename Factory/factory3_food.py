from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass


class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni pizza")


class VeggiePizza(Pizza):
    def prepare(self):
        print("Preparing Veggie pizza")


class MargheritaPizza(Pizza):
    def prepare(self):
        print("Preparing Margherita pizza")


class PizzaFactory:
    def create_some_pizza(self, pizza_type):
        if pizza_type.lower() == "margherita":
            return MargheritaPizza()

        if pizza_type.lower() == "pepperoni":
            return PepperoniPizza()

        if pizza_type.lower() == "veggie":
            return VeggiePizza()


# Client code
pizza_factory = PizzaFactory()
pizza_type = input("what pizza do you want to try today ? ")
pizza = pizza_factory.create_some_pizza(pizza_type)
pizza.prepare()