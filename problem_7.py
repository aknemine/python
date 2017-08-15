list = [2]
time = 0
count = 1
i = 3
while(count < 10001):
    time = 0
    for j in range(2, int(i ** 0.5) + 1):
        if(i % j == 0):
            time = time + 1
    if(time == 0):
        list.append(i)
        count = count + 1
    i += 1
print(list[count - 1])
