"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
     # Create an instance of the `Account` class with initial interest of 0
    account = Account(balance, 0)

    # Calculate the monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate the interest earned
    interest_earned = account.balance * monthly_interest_rate * months

    # Update the CD account balance
    updated_balance = account.balance + interest_earned

    # Pass the updated_balance to the set_balance method using the instance of the Account class
    account.set_balance(updated_balance)

    # Pass the interest_earned to the set_interest method using the instance of the Account class
    account.set_interest(interest_earned)

    return updated_balance, interest_earned
