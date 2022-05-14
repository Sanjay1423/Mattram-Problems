string = input()
str_list = []
for i in string:
    if i != ' ':
        str_list.append(i)
    else:
        continue
print(''.join(str_list))
