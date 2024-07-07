dict1 = {}
n = int(input("Enter the number of elements in the dictionary: "))
for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = int(input(f"Enter value for key '{key}': "))
    dict1[key] = value
items = list(dict1.items())
for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]
sorted_dict = {key: value for key, value in items}
print("The sorted dictionary by value is:")
for key, value in sorted_dict.items():
    print(f"{key}: {value}")
