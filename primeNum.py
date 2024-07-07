sum = 0
for num in range(2, 101):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        sum += num
print("The sum of all prime numbers between 1 and 100 is:", sum)
