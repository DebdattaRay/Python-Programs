ctr = 0
num = eval(input("Enter a number : "))
for i in range(1,num+1):
    if(num % i == 0):
        ctr = ctr + 1
if(ctr == 2):
    print("Prime Number")
elif(ctr>2):
        print("Not Prime Number")
