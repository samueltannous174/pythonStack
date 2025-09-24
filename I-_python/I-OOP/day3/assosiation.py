from bank import BankAccount;


class User:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.account_balance = initial_balance
        self.account = BankAccount(int_rate=0.02, balance=0)  


    def make_withdrawal(self, amount):
        if amount <= 0:
            return self
            
        if amount > self.account_balance:
            print(f"Current balance: ${self.account_balance}")
            return self
            
        self.account_balance -= amount
        print(f"Withdrawal of ${amount} successful")
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        if amount <= 0:
            print("Transfer amount must be positive")
            return self
            
        if amount > self.account_balance:
            print(f"Current balance: ${self.account_balance}")
            return self
        
        self.account_balance -= amount
        other_user.account_balance += amount

        print(f"Transfer of ${amount} from {self.name} to {other_user.name} completed successfully")
        return self
