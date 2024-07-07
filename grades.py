math = eval(input("Enter maths marks      : "))
phy = eval(input("Enter physics marks     : "))
bio = eval(input("Enter biology marks     : "))
chem = eval(input("Enter chemistry marks  : "))
comp = eval(input("Enter computer marks   : "))
perc = (math + phy + bio + chem + comp) / 5
if(perc >= 90):
    print("GRADE A")
elif(perc >= 80):
    print("GRADE B")
elif(perc >= 70):
    print("GRADE C")
elif(perc >= 60):
    print("GRADE D")
else:
    print("FAIL")
