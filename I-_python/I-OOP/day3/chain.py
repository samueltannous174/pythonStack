class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self  
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self  
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self 
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self  

guido = User("Guido van Rossum", "guido@python.org")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(50)
guido.display_user_balance()

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


monty = User("Monty Python", "monty@python.org")

guido.make_deposit(500)\
     .transfer_money(monty, 250)\
     .display_user_balance()

monty.display_user_balance()