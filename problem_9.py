def kare(x):
    return x ** 2

for i in range(5, 1000):
    for j in range(4, i):
        for k in range(3, j):
            if(i + j + k == 1000):
                f = kare(i)
                e = kare(j)
                d = kare(k)
                if(e + d == f):
                    print(i * j * k)
