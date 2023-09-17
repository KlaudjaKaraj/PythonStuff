class Customer: # creating a Customer class
    def __init__(self, name, email): # Customers need to have a name, email and list of purchases
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, item): # Customers need to have a purchase method
        self.purchases.append(item)
        print(f"{self.name} purchased {item.name}")

    def print_purchases(self): # Customers need to have a print purchases method
        print(f"{self.name}'s Purchases:") # so we can keep track of the purchases
        for item in self.purchases:
            print(f"- {item.name}")

class Item: # creating a Item class
    def __init__(self, name, price): # Items need to have a name and a price
        self.name = name
        self.price = price

class VIPCustomer(Customer): # creating a VIP customer class, inheriting from the Customer Class
    def __init__(self, name, email, membership_level):
        super().__init__(name, email) # inheriting init of Customer class
        self.membership_level = membership_level # but adding membership stuff to it
        self.discount = 0.1                      # VIPcustomers need to have a membership level but discount is set already

    def purchase(self, item): # completely recreating purchase method
        discounted_price = item.price * (1 - self.discount) # for some discount application
        self.purchases.append(item)
        print(f"{self.name} (VIP) purchased {item.name} for ${discounted_price:.2f} (Original Price: ${item.price:.2f})")

my_customer = Customer("Alice", "alice@example.com")
my_item = Item("Smartphone", 1000)
my_customer.purchase(my_item) # Output: "Alice purchased Smartphone"
my_customer.print_purchases() # Output: "Alice's Purchases: - Smartphone"

my_vip_customer = VIPCustomer("Bob", "bob@example.com", "Gold")
my_item2 = Item("Laptop", 1500)
my_vip_customer.purchase(my_item2) # Output: "Bob (VIP) purchased Laptop for $1350.00 (Original Price: $1500.00)"
my_vip_customer.print_purchases() # Output: "Bob's Purchases: - Laptop"