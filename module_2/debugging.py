# This program determines whether the customer has sufficient funds for items purchased.
# Cost of items are stored in a list.
# The program accepts the customer's name and the amount of money they have.
# The program then checks if the customer has sufficient funds to purchase the items.
# If the customer has sufficient funds, the program will print the customer's name and the amount of money they have

ITEM_COST = 5.00
MIN_YEARS_WITH_BANK_ACCOUNT = 3

# Get the customer's name and the amount of money they have
customer_name = input("Enter your name: ")  

money_in_bank_account = (input("Enter the amount of money in your bank account: "))

# Check if the customer has sufficient funds to purchase the items

if money_in_bank_account >= ITEM_COST:
    print(f"{customer_name}, you have sufficient funds to purchase the item.")

else:
    print(f"{customer_name}, you do not have sufficient funds to purchase the item.")

# Check if the customer has been with the bank for at least 3 years

years_with_bank_account = int(input("Enter the number of years you have been with the bank account: "))
if years_with_bank_account >= MIN_YEARS_WITH_BANK_ACCOUNT:
    print(f"{customer_name}, you have been with the bank for at least {MIN_YEARS_WITH_BANK_ACCOUNT} years.")

else:
    print(f"{customer_name}, you have not been with the bank for at least {MIN_YEARS_WITH_BANK_ACCOUNT} years.")

