fact = 1
num = int(input("Enter number : "))
for i in range(1, num+1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")