'''
Module providing a series of functions used
to emulate an atm machine

# Gioele Amendola
# 29/04/2024

# Create a function that simulates an ATM machine.
# Initialize an account with a starting balance.
# Allow the user to perform transactions such as deposit, withdraw, and check balance.
# Validate transactions against the account balance and available funds.
# Provide appropriate feedback to the user for each transaction.
'''
# This is only for example purposes
import random


def atm_machine(balance: float = random.randint(1000, 10000)):
    '''
    Main menu for the atm machine simulator

    Args:
        balance (float, optional): Balance of an account.
        "Defaults to random.randint(1000,10000) - only for example purposes".
    '''

    print("Welcome to the ATM machine")

    funds: float = balance
    transaction: float = 0
    choose: int = -1

    while True:
        print("\nChoose a transaction:\n1. Deposit\n2. Withdraw\n3. Check Balance\n0. Exit")
        # Select the function to go to based on input number
        try:
            choose = int(input("\n> "))
        except ValueError:
            print("Input Not Valid. Retry.")

        if choose == 1:
            transaction = deposit(balance)
            balance += transaction
            print("\nTransaction Accepted")

        elif choose == 2:
            if funds <= 10:
                print("\nImpossible transaction.")
            else:
                transaction = withdraw(funds)
                funds -= transaction
                balance -= transaction
                print("\nTransaction Accepted")

        elif choose == 3:
            check_balance(balance, funds)

        elif choose == 0:
            return


def deposit(balance: float) -> float:
    '''
    Used to deposit an amount of money in the balance

    Args:
        balance (float): balance of an account.

    Raises:
        ValueError: The amount to add to the balance is less then 10.

    Returns:
        float: The amount of the deposit
    '''

    print("Deposit")
    print(f"current balance: ${balance:.2f}")

    while True:
        try:
            transaction: float = float(
                input(f"\n\t{'Enter Deposit Amount':<10}\n\t$"))
            if transaction < 10:
                raise ValueError
        except ValueError:
            print("Amount Invalid")
        else:
            break

    return transaction


def withdraw(funds: float) -> float:
    '''
    Used to withdraw an amount of money from the balance

    Args:
        funds (float): The amount of money permittable to withdraw

    Raises:
        ValueError: The amount of money to withdraw is less then 10.
        ValueError: The amount of money to withdraw surpasses the amount of funds.

    Returns:
        float: The amount of money to withdraw.
    '''

    print("Withdraw")
    print(f"current available funds: ${funds:.2f}")

    while True:
        try:
            transaction: float = float(
                input(f"\n\t{'Enter Withdrawal Amount':<10}\n\t$"))
            if transaction < 10:
                raise ValueError
            if transaction > funds:
                raise ValueError
        except ValueError:
            print("Amount Invalid")
        else:
            break

    return transaction


def check_balance(balance: float, funds: float):
    '''
    Used to print on console everything about an account.

    Args:
        balance (float): Balance of the account.
        funds (float): Funds of the account.
    '''

    print(f"\t\t{'Account Balance':<10}")
    print(f"balance:\t ${balance:<10.2f}")
    print(f"available funds: ${funds:<10.2f}\n")
    input()


# Example Test:
atm_machine()
