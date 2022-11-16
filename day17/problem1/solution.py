input = input()

original_array = [int(i) for i in input]  # ! => [1, 1, 4, 2, 1, 3]
sorted_array = sorted(original_array)  # ! => [1, 1, 1, 2, 3, 4]
count = 0

for i in range(0, len(original_array)):
    if original_array[i] != sorted_array[i]:
        count += 1

print(count)
