numbers = input("Enter the list of integers separated by space: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
target_sum = int(input("Enter the target sum: "))
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pairs.append((numbers[i], numbers[j]))
print("Pairs of integers that sum up to", target_sum, "are:")
for pair in pairs:
    print(pair)
