sayi = 2
t = 0
sayac = 1
i = 3
for i in range(3, 2000000, 2):
    t = 0
    for j in range(3, int(i ** 0.5) + 1, 2):
        if(i % j == 0):
            t = t + 1
            break
    if(t == 0):
        sayi += i
print(sayi)

