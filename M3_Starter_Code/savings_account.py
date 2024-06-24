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

# Example usage
if __name__ == "__main__":
    initial_balance = 1000  # Example balance
    apr = 0.05  # Example annual interest rate (5%)
    duration = 6  # Example duration in months

    new_balance, earned_interest = create_savings_account(initial_balance, apr, duration)
    print(f"New Balance: {new_balance}")
    print(f"Interest Earned: {earned_interest}")

    
    

    # Calculate interest earned
   

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
