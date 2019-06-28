#######################################
# income tax 
# function
# input: income
# return: tax
#######################################

def income_tax(income):
    if income <= 85528:
        tax = 0.18*income-556.02
    elif income > 85528:
        tax = 14839.02 + 0.32*(income-85528)
        
    tax = round(tax, 0)
    if tax < 0:
        tax = 0.0
    else:
        None
    return tax

