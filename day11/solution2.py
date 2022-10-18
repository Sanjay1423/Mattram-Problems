input = input()
array1 = [int(i) for i in input]
array2 = [int(i) for i in set(input)]
string = ""
for j in range(len(array2)):
    if j == 0:
        pass
    else:
        array2.remove(min(array2))
    for i in array1:
        if i == min(array2):
            string += str(i)


print(string)
