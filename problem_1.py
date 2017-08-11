#1000 in altındaki 3 veya 5 in katları


tp = 0
for i in range(1000):
    if(i % 3 == 0):
        tp += i
    elif(i % 5 == 0):
        tp += i
print(tp)

