string = input()
arr = []
for i in string:
    if i == '0':
        arr.append('1')
    else:
        arr.append(i)

string2 = ''.join(arr)
print(string2)
