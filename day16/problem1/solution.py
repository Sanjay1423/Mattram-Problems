
n = input()  # ! => '35'
array1 = [int(i) for i in n]  # ! => [3,5]
Sum1 = sum(array1)  # ! => 8
array2 = []

for i in range(int(n)-1, 10, -1):  # ! = range(34, 10, -1)
    array3 = list(str(i))  # ! =>
    Sum2 = sum([int(i) for i in array3])  # ! =>
    if Sum2 > Sum1:
        print(i)
        break
else:
    print(int(n))
