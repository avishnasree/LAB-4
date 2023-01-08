# 5. Write a program to add variable length integer arguments passed to the
# function. [Also demo the use of docstrings]

def add_integers(*args):
    """
       This function adds a variable number of integers and returns the sum.

       Parameters:
       args (int): variable length list of integers

       Returns:
       int: sum of the integers
       """
    sum = 0
    for i in args:
        sum += i
    return sum

print(add_integers(1, 2, 3, 4, 5))
print(add_integers(10, 20, 30))
print(add_integers(100))
