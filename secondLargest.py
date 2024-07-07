numbers = []
n = int(input("Enter the number of elements in the tuple: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    numbers.append(element)
numbers_tuple = tuple(numbers)
if numbers_tuple[0] > numbers_tuple[1]:
    largest = numbers_tuple[0]
    second_largest = numbers_tuple[1]
    index = 2
else:
    largest = numbers_tuple[1]
    second_largest = numbers_tuple[0]
    index = 1

# Iterate through the rest of the tuple
for i in range(index, len(numbers_tuple)):
    if numbers_tuple[i] > largest:
        second_largest = largest
        largest = numbers_tuple[i]
    elif numbers_tuple[i] > second_largest and numbers_tuple[i] != largest:
        second_largest = numbers_tuple[i]

print("The second largest number is:", second_largest)
