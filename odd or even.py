# 2. Write a program using functions and return statements to check whether a
# number is even or odd.

def check_even_odd(num):
  if num % 2 == 0:
    return "Even"
  else:
    return "Odd"

print(check_even_odd(32))
print(check_even_odd(3))