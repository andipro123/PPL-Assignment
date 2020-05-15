#find first 10 amicable numbers
import math

def sumOfDivisor(x):
    sum = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if x / i != i:
                sum += i + (x / i)
            else:
                sum += i
    return sum

def amicable(x, y):
    return sumOfDivisor(x) == y and sumOfDivisor(y) == x

count = 0
i = 1
while count < 10:
    j = sumOfDivisor(i)
    if amicable(i, j):
        if i < j:
            print(i, j)
            count += 1
    i += 1

