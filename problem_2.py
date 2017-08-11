sum = 0
fibo = 1
first = 1
this = 0
while(first < 4000000):
    if(first % 2 == 0):
        sum += first
    fibo += this
    this = first
    first = fibo
print(sum)

