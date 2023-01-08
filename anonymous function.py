# 7. Write a program to display powers of 2 using anonymous function.[Hint use map and lambda function)

terms = 10
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
