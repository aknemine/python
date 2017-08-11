count = 0
num = 600851475143
for i in range(2, num):
    if(num % i == 0):
        for n in range(2, i):
            if(i % n == 0):
                count += 1
        if(count == 0):
            print(i)
        else:
            break

