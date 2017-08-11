def ters(sayi):
    yedek = sayi
    b = 0
    a = 0
    while(sayi > 0):
        a = sayi % 10
        b = (b * 10) + a
        sayi = int(sayi / 10)
    if(b == yedek):
        return yedek
    else:
        return 0

palindrom = 0
psayi = 1
for i in range(100, 1000):
    for n in range(100, 1000):
        carp = i * n
        psayi = ters(carp)
        if(psayi != 0):
            if(psayi >= palindrom):
                palindrom = psayi
print(palindrom)

