i = 20
j = 0
while(j != 20):
    i += 20
    for j in range(11, 21):
        if(i % j != 0):
            break
print(i)
