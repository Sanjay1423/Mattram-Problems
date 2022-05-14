string_list = list(input().split())
n_times = 0
length = []
for i in string_list:
    length.append(len(i))
max_value = max(length)
for i in string_list:
    if len(i) == max_value:
        print(i)
        break


