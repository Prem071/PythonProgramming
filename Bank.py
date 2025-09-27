# 1. customer
# 2. account
# 3. bank

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def addCustomers(self, customers_list):
        self.customers.append(customers_list)
        print('Customers are added to the Bank')

    def addAccounts(self, accounts_list):
        self.accounts.append(accounts_list)
        print('Accounts are added to the Bank')

    # def getinfo(self):
    #     print([i.name for i in self.customers])
    #     print('--------------------------')
    #     print([i.acc_no for i in self.accounts])
    #     print('--------------------------')
    #     print([i.balance for i in self.accounts])

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.accounts = []

    def openAccount(self, initial_deposit, bank):
        new_acc = Account(len(bank.accounts)+1, self, initial_deposit)
        self.accounts.append(new_acc)
        bank.addAccounts(new_acc)
        print(f'Account opened with account number {new_acc.acc_no} and balance {new_acc.balance}')


class Account:
    def __init__(self, acc_no, customer, initial_deposit):
        self.acc_no = acc_no
        self.customer = customer
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. New balance is {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance is {self.balance}')

    def getInfo(self):
        print(f'Account Number: {self.acc_no}, Customer: {self.customer.name}, Balance: {self.balance}')

class BankApp:
    bank = Bank()

    # Adding Customers
    c1 = Customer(1, 'prem')
    c2 = Customer(2, 'siddu')
    bank.addCustomers([c1, c2])
    # bank.addCustomers(c2)

    # Customers opening accounts
    c1.openAccount(1000, bank)
    c2.openAccount(500, bank)

    # Performing transactions
    acc1 = c1.accounts[0]
    acc2 = c2.accounts[0]

    acc1.deposit(200)
    acc1.withdraw(150)

    acc2.deposit(300)
    acc2.withdraw(1000) 

    # Displaying account info
    acc1.getInfo()
    acc2.getInfo()

    

