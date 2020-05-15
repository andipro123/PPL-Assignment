
def mean(x):
    sum = 0
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            sum += (1/i)
            count += 1
    return (count / sum)

count = 0
i = 1

while count < 10:
    x = mean(i)
    if round(x, 10) == int(x):
        count += 1
        print(i)
    i += 1
