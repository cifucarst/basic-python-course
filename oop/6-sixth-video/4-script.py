#!/usr/bin/env python3

class BankAccount:
    """Represents a bank account with its account number, owner, and balance."""

    def __init__(self, account_number: str, owner: str, initial_balance: int = 0) -> None:
        """
        Initializes a BankAccount object with the given account number, owner, and initial balance.

        Args:
            account_number: The account number of the bank account (str).
            owner: The owner of the bank account (str).
            initial_balance: The initial balance of the bank account (int).
        """
        self.account_number = account_number
        self.owner = owner
        self.__balance = initial_balance  # private attribute

    def deposit_money(self, amount: int) -> None:
        """
        Deposits money into the bank account.

        Args:
            amount: The amount of money to deposit (int).
        """
        if amount > 0:
            self.__balance += amount
            print(f'\n[+] Current balance: {self.__balance}')
        else:
            print(f'\n[!] The deposit amount is incorrect')

    def withdraw_money(self, amount: int) -> None:
        """
        Withdrawals money from the bank account.

        Args:
            amount: The amount of money to withdraw (int).
        """
        if amount > 0:
            if amount > self.__balance:
                print(f'\n[!] The withdrawal amount exceeds the current balance')
            else:
                self.__balance -= amount
                print(f'\n[+] Current balance: {self.__balance}')
        else:
            print(f'\n[!] The withdrawal amount is incorrect')

    def show_balance(self) -> str:
        """
        Returns a string representation of the current balance.

        Returns:
            A string representing the current balance.
        """
        return f'\n[+] The current balance is: {self.__balance}'


# Creates a BankAccount object
manolo = BankAccount("23456", "manolo vieira", 1500)

# Deposits 500 euros into the account
manolo.deposit_money(500)

# Withdraws 200 euros from the account
manolo.withdraw_money(200)

# Prints the current balance
print(manolo.show_balance())