class BankAccount:
    def __init__(self):
        self.balance = 0 

    def deposit(self, value):
        self.balance += value
        print(f"Deposited ${value}. Current balance: ${self.balance}")

    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
            print(f"Withdrew ${value}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def show_balance(self):
        print(f"Current balance: ${self.balance}")

account1 = BankAccount()

account1.deposit(100)
account1.withdraw(50)
account1.show_balance()
