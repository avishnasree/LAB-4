# 8. Write a program to sum the series 1/1! + 4/2! + 27/3! + ..... + nth term. [ HintUse a function to find the factorial of a number].

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += (i**i) / factorial(i)
    return sum

print(sum_series(1)) # should print 1/1! = 1
print(sum_series(2)) # should print 1/1! + 4/2! = 1 + 2 = 3
print(sum_series(3)) # should print 1/1! + 4/2! + 27/3! = 1 + 2 + 6 = 9
print(sum_series(4)) # should print 1/1! + 4/2! + 27/3! + 256/4! = 1 + 2 + 6 + 24 = 33

