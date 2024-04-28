class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} made. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of ${amount} made. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest_rate = interest_rate / 100

    def calculate_interest(self):
        monthly_interest = self.balance * self.interest_rate
        self.deposit(monthly_interest)
        print(f"Monthly interest of ${monthly_interest:.2f} added to the account.")

savings_account = SavingsAccount(0.5)
savings_account.deposit(1000)
savings_account.calculate_interest()
savings_account.check_balance()
