n = int(input("Eter the number range : "))
sum = 0.0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum -= 1 / i
    else:
        sum += 1 / i
print("The sum of the series is:", sum)
