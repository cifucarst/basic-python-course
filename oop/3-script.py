#!/usr/bin/env python3


class BankAccount:
    # constructor method
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    # deposit money method
    def deposit_money(self, amount):
        self.balance += amount
        return f"\n[+] {amount} euros deposited, current balance is {self.balance} euros"

    # withdraw money method
    def withdraw_money(self, amount):
        if amount > self.balance:
            return f"\n[!] Operation denied: Insufficient funds\n"

        self.balance -= amount
        return f"\n[+] {amount} euros withdrawn, current balance is {self.balance} euros"



manolo = BankAccount("187263", "Manolo Vieira", 1000)
print(manolo.deposit_money(500))
print(manolo.withdraw_money(900))
