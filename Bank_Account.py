class BankAccount():
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return (self.balancei)

    def display_account_info(self):
        print(f"Account number: {self.account_number} \n Account holder:{self.account_holder} \n current balance:{self.balance}")
              
new_bank_account = BankAccount(122, "mr A", 7)

print(new_bank_account.get_balance())

new_bank_account.deposit(1000000)
print(new_bank_account.get_balance())

new_bank_account.withdraw(10000)
print(new_bank_account.get_balance())

new_bank_account.display_account_info()
