def sum(num):
    sm = 0
    for i in range(1, num+1):
        sm = sm + (square(i))
    return sm


def square(a):
    this = a ** 2
    return this


def sum1(x):
    summ = 0
    for i in range(1, x+1):
        summ = summ + i
    b = (square(summ))
    return b
sub = sum1(100) - sum(100)
print(sub)
