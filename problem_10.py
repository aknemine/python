number = 2
for i in range(3, 2000000, 2):
    time = 0
    for j in range(3, int(i ** 0.5) + 1, 2):
        if(i % j == 0):
            time = time + 1
            break
    if(time == 0):
        number += i
print(number)
