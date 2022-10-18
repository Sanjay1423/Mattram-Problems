string = input()
unique = set(string)
count_list = [string.count(i) for i in unique]


for i in count_list:
    if count_list[0] == i:
        pass
    else:
        print('false')
        break

else:
    print('true')
