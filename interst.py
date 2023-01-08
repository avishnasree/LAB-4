#1. Write a program using functions to calculate the simple interest. Suppose the
# customer is a senior citizen. He is being offered a 12 percent rate of interest,
# for all other customers, the rate of interest is 10 percent.

def calculate_interst(principal,year,senior_citizen):
    if senior_citizen:
        rate = 12
    else:
        rate = 10
    interst = principal * year * rate
    return interst
print(calculate_interst(10000,5, True))
print(calculate_interst(10000,5, False))