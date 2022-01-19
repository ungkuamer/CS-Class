"""
Repair line 20,31 on the initialization of new savings and current account

Problems:
- How to set account holder name after saving/current account is initialize
 
Solutions:
- Repair subclass account initialization
- Fix during new account instances at end of code

"""

import random

class BankAccount:

    def createNewAccount(self, accountHolder=None):
        self.__AccountHolderName = accountHolder
        self.__IBAN = random.randint(111111111111, 999999999999)

    def setAccountHolderName(self, holderName):
        self.__AccountHolderName = holderName

    def getAccountHolderName(self):
        return self.__AccountHolderName

    def getIBAN(self):
        return self.__IBAN

class PersonalAccount:
    def __init__(self):
        BankAccount.createNewAccount() # <---- Here
        self.__monthlyPayment = False
        self.__overdraftLimit = 0

    def paymentStatus(self):
        return self.__monthlyPayment

    def getOverdraftLimit(self):
        return self.__overdraftLimit

class SavingsAccount:
    def __init__(self, holderName=None, IBAN=None):
        BankAccount.createNewAccount() # <---- Here
        self.__accBalance = random.randint(0, 20000)
        self.__interestRate = random()

    def getBalance(self):
        return self.__accBalance

    def getInterestRate(self):
        return self.__interestRate


