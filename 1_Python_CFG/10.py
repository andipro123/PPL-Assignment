import math

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
a = int(input("Enter value of a: "))

for i in range(0, n):
    print(a * (r ** i))
    