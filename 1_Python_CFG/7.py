#Armstrong numbers in a given range

def armstrongCheck(x):
    sum = 0
    while x:
        y = x % 10
        sum += y ** 3
        x = int(x / 10)
    return sum

x = int(input("Enter left limit of the range: "))
y = int(input("Enter right limit of the range: "))

for i in range(x, y + 1):
    if i == armstrongCheck(i):
        print(i)

