d1 = eval(input("1st date  : "))
m1 = eval(input("1st month : "))
y1 = eval(input("1st year  :"))

d2 = eval(input("2nd date  : "))
m2 = eval(input("2nd month : "))
y2 = eval(input("2nd year  :"))

if(d1>31 or d2>31 or m1>12 or m2>12):
    print("Invalid date, Re-enter.")
if(y1<y2):
    print(f"The earlier date is {d1}/{m1}/{y1}")
elif(y1 == y2):
    if(m1<m2):
        print(f"The earlier date is {d1}/{m1}/{y1}")
    elif(m1 == m2):
        if(d1<d2):
            print(f"The earlier date is {d1}/{m1}/{y1}")
        else:
            print(f"The earlier date is {d2}/{m1}/{y1}")
    else:
        print(f"The earlier date is {d2}/{m2}/{y2}")
else:
    print(f"The earlier date is {d2}/{m2}/{y2}")
            