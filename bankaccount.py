
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
      

    def deposit(self, account_number, amount):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount    
        print(f"${amount} has been deposited into account {self.account_number}.")

    def withdraw(self, amount):
        amount = float(input("Enter amount to be withdraw: "))
        if amount > self.balance:
            print("You have insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from {self.account_number}.")

    def view_balance(self):
        print(f"Account {self.account_number} existing balance is: ${self.balance}")
 

    def print_user_details(self):
        print("Account Number:", self.account_number)
        print(f"Balance: ${self.balance}\n")   


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, balance=0):
        account = BankAccount(account_number, balance)
        self.accounts.append(account)
        print(f"Account {account_number} is created.")
    
    def get_account(self, account_mumber):
        for account in self.accounts:
            if account.account_number == account_mumber:
                return account
        else:
            print ("Account is not found.")

      
print("========================================================================================")
print(                       "WELCOME TO JVE BANKING SYSTEM"                                    )
print("========================================================================================")

'''
# Creating an object of class
Bank = Bank()


# Calling functions with that class to CREATE NEW ACCOUNT WITH DEPOSIT
Bank.create_account(7008, 700)
account = Bank.get_account(7008)
print(account.view_balance())
'''
'''
# Calling functions with that class to DEPOSIT
account_one = BankAccount (7008,700)
account_one.deposit(7008, 1000)
print(account_one.view_balance())
'''
'''
# Calling functions with that class to DO SUCCESFUL WITHDRAW
account_one = BankAccount (7008, 1700)
account_one.withdraw(1300)
print(account_one.view_balance())
'''

# Calling functions with that class to  WITHDRAW but INSUFFICIENT BALANCE
account_one = BankAccount (7008, 400)
account_one.withdraw(500)
print(account_one.view_balance())