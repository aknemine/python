def reverse(num):
    hide = num
    b = 0
    a = 0
    while(num > 0):
        a = num % 10
        b = (b * 10) + a
        num = int(num/ 10)
    if(b == hide):
        return hide
    else:
        return 0

palindrome = 0
number = 1
for i in range(100, 1000):
    for j in range(100, 1000):
        mult = i * j
        number = reverse(mult)
        if(number != 0):
            if(number >= palindrome):
                palindrome = number
print(palindrome)
