month = input("Enter Your Month : ")
if(month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december"):
    print("Number of days : 31")
elif(month == "february"):
    print("Number of days : 28 or 29(leap year)")
else:
    print("Number of days : 30")
