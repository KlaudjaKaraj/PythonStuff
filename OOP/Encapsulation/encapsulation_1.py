class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number  # Public attribute
        self.account_holder = account_holder  # Public attribute
        self.__balance      = 0 # PRIVATE attribute (can't be accessed directly)

    # Public method
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit successful. Current balance: ${self.__balance}")

    # Public method
    def withdraw(self, amount):
        if self.__check_balance(amount):  # PRIVATE method
            self.__balance -= amount
            print(f"Withdrawal successful. Current balance: ${self.__balance}")
        else:
            print("Insufficient balance.")

    # PRIVATE method (can't be accessed directly - internal helper)
    def __check_balance(self, amount):
        return self.__balance >= amount

account = BankAccount("14141414141", "Bruce Wayne")
account.deposit(500)
account.withdraw(100)
#print(account.__check_balance(400)) won't work
print(account._BankAccount__check_balance(400)) # works, but how dare us