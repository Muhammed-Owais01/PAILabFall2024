class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"New Balance After Deposit: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"New Balance After Withdrawal: {self.balance}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

obj1 = BankAccount(12390123, 200, "20/10/2003", "Owais")
obj1.check_balance()
obj1.deposit(500)
obj1.withdraw(200)