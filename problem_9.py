def square(x):
    return x ** 2

for i in range(5, 1000):
    for j in range(4, i):
        for k in range(3, j):
            if(i + j + k == 1000):
                f = square(i)
                e = square(j)
                d = square(k)
                if(e + d == f):
                    print(i * j * k)
