# 3.Write a function called compare which takes two strings S1 and S2 and an integer n as arguments. The function should return True if the first n characters of both the strings are the same else the function should return False

def compare(S1, S2, n):
    if S1[:n] == S2[:n]:
        return True
    else:
        return False
S1 = "Hello W"
S2 = "Hello World"
n = 8
if compare(S1, S2, n):
    print("True")
else:
    print("False.")