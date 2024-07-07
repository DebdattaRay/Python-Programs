print("*** User Choice Calculator ***")
print("****** Application Menu ******")
print("For Addition       : 1")
print("For Subtraction    : 2")
print("For Multiplication : 3")
print("For Division       : 4")

print("******************************")
print("******************************")
print()
ch = int(input("Enter Your Choice :"))
if(ch == 1):
    a = eval(input("enter no : "))
    b = eval(input("enter another no :"))
    sum = a+b
    print(f"addition : {sum}")
if (ch == 2):
     a = eval(input("enter no : "))
     b = eval(input("enter another no :"))
     diff = a - b
     print(f"difference is : {diff}")
if(ch == 3):
     a = eval(input("enter no : "))
     b = eval(input("enter another no :"))
     mult = a * b
     print(f"multiplication is : {mult}")
if(ch == 4):
     a = eval(input("enter no : "))
     b = eval(input("enter another no :"))
     div = a % b
     print(f"division is {div}")