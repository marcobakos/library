#


class Account:
    # Define an __init__ constructor method with attributes shared by all accounts:
    def __init__(self, acct_nbr, opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit

    # Define a __str__ mehthod to return a recognizable string to any print() command
    def __str__(self):
        return f'${self.balance:.2f}'

    # Define a universal method to accept deposits
    def deposit(self, dep_amt):
        self.balance += dep_amt

    # Define a universal method to handle withdrawals
    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
        else:
            print('Funds Unavailable')    # changed "return" to "print"


#
class Checking(Account):
    def __init__(self, acct_nbr, opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr, opening_deposit)

    # Define a __str__ method that returns a string specific to Checking accounts
    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


#
class Savings(Account):
    def __init__(self,acct_nbr, opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr, opening_deposit)

    # Define a __str__ method that returns a string specific to Savings accounts
    def __str__(self):
        return f'Savings Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


#
class Business(Account):
    def __init__(self,acct_nbr, opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr, opening_deposit)

    # Define a __str__ method that returns a string specific to Business accounts
    def __str__(self):
        return f'Business Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


#
class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN

        # Create a dictionary of accounts, with lists to hold multiple accounts
        self.accts = {'C': [], 'S': [], 'B': []}

    def __str__(self):
        return self.name

    def open_checking(self, acct_nbr, opening_deposit):
        self.accts['C'].append(Checking(acct_nbr, opening_deposit))

    def open_savings(self, acct_nbr, opening_deposit):
        self.accts['S'].append(Savings(acct_nbr, opening_deposit))

    def open_business(self, acct_nbr, opening_deposit):
        self.accts['B'].append(Business(acct_nbr, opening_deposit))

    # rather than maintain a running total of deposit balances,
    # write a method that computes a total as needed
    def get_total_deposits(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Account: {self.name}  - Combined Deposits: ${total:.2f}')  # added precision formatting here


#
def make_dep(cust, acct_type, acct_num, dep_amt):
    """
    make_dep(cust, acct_type, acct_num, dep_amt)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acct_num  = integer
    dep_amt   = integer
    """
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.deposit(dep_amt)


#
def make_wd(cust, acct_type, acct_num, wd_amt):
    """
    make_wd(cust, acct_type, acct_num, wd_amt)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acct_num  = integer
    wd_amt    = integer
    """
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.withdraw(wd_amt)


#
# Execução do pgm
#
# Criar Cliente
# Abrir Contas (C,S,B) para o Cliente
# Fazer Depositos nas diferentes contas (C,S,B)
# Fazer Retiradas nas diferentes contas (C,S,B)
#
bakos=Customer("Bakos", 1955)
#
print(bakos)
#
bakos.open_checking(1001, 500.00)
#
bakos.open_savings(2001, 450.00)
#
bakos.open_business(3001, 350.00)
#
bakos.get_total_deposits()
#
make_dep(bakos, 'C', 1001, 50.55)
make_dep(bakos, 'S', 2001, 100.66)
make_dep(bakos, 'B', 3001, 200.77)
#
bakos.get_total_deposits()
