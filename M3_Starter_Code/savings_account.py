"""Import the Account class from the Account.py file."""
from Account import Account

balance = 1000 
interest = 0  

my_account = Account(balance, interest)

print(f"Initial Balance: {my_account.balance}")
print(f"Initial Interest: {my_account.interest}")

my_account.set_balance(2000)
my_account.set_interest(0.03)

print(f"Updated Balance: {my_account.balance}")
print(f"Updated Interest: {my_account.interest}")


# Define a function for the Savings Account
# main.py
from Account import Account

def create_savings_account(balance, interest_rate, months):
    
    # Create an instance of Account
    account = Account(balance, interest_rate)

    # Calculate the monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate the interest earned
    interest_earned = account.balance * monthly_interest_rate * months

    # Update the account balance
    updated_balance = account.balance + interest_earned
    account.set_balance(updated_balance)

    # Pass the interest earned to the set_interest method
    account.set_interest(interest_earned)

    return updated_balance, interest_earned

