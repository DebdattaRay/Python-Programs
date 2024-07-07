n = int(input("Enter the value of n: "))
series_str = ""

for i in range(1, n + 1):
    if i % 2 == 0:
        series_str += f" - 1/{i}"
    else:
        if i == 1:
            series_str += f"1/{i}"
        else:
            series_str += f" + 1/{i}"

print("The series is:", series_str)
