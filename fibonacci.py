n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci series:")
for i in range(n+1):
    print(a, end=",")
    a, b = b, a + b
