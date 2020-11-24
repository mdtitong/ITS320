# Create a program that will calculate the weekly average tax withholding for a customer, given the following weekly income guidelines:
# Income less than $500: tax rate 10%
# Incomes greater than/equal to $500 and less than $1500: tax rate 15%
# Incomes greater than/equal to $1500 and less than $2500: tax rate 20%
# Incomes greater than/equal to $2500: tax rate 30%
# Store the income brackets and rates in a dictionary.
# Write a statement that prompts the user for an income and then looks up the tax rate from the dictionary and prints the income, tax rate, and tax.
# Develop Python code that implements the program requirements.

# ------Income Brackets------
tax_rate = {499: "10%", 1499: "15%", 2499: "20%", 2500: "30%"}

# ------user input weekly income-------
income = float(input("Enter weekly income: "))

# ------Income less than $500: tax rate 10%------
if(income < 500):
    tax = income * 0.1
    print("Your weekly income is $%.2f and your tax rate is %s" %
          (income, tax_rate[499]))
    print("Tax to your income is: $%.2f" % tax)

# ------Incomes greater than/equal to $500 and less than $1500: tax rate 15%------
elif(income < 1500):
    tax = income * 0.15
    print("Your weekly income is $%.2f and your tax rate is %s" %
          (income, tax_rate[1499]))
    print("Tax to your income is: $%.2f" % tax)

# ------Incomes greater than/equal to $1500 and less than $2500: tax rate 20%------
elif(income < 2500):
    tax = income * 0.20
    print("Your weekly income is $%.2f and your tax rate is %s" %
          (income, tax_rate[2499]))
    print("Tax to your income is: $%.2f" % tax)

# ------Incomes greater than/equal to $2500: tax rate 30%------
else:
    tax = income * 0.30
    print("Your weekly income is $%.2f and your tax rate is %s" %
          (income, tax_rate[2500]))
    print("Tax to your income is: $%.2f" % tax)
