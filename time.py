curTime = eval(input("Enter the current time : "))
phase = eval(input("Enter '1' for AM and '2' for PM : "))
addHrs = eval(input("Enter hours ahead : "))
futTime = curTime + addHrs
if(phase == 1):
    if(futTime>24):
        newTime = futTime - 12
        print("The new time is :",newTime,"PM")
    else:
        newTime = futTime
        print("The new time is : ",newTime,"AM")
elif(phase == 2):
    if(futTime>=12):
        newTime = futTime - 12
        print("The new time : ",newTime,"AM")
    else:
        newTime = futTime
        print("The new time : ",newTime,"PM")