liste = [2]
t = 0
sayac = 1
i = 3
while(sayac < 10001):
    t = 0
    for j in range(2, int(i ** 0.5) + 1):
        if(i % j == 0):
            t = t + 1
    if(t == 0):
        liste.append(i)
        sayac = sayac + 1
    i += 1
print(liste[sayac - 1])
