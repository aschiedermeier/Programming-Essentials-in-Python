#######################################
# income tax
# program to get income, call function and output tax
#######################################

from tax_function import income_tax

income = float(input("Enter the annual income: "))
tax = income_tax(income)
print("The tax is:", tax, "Schmeckles")
