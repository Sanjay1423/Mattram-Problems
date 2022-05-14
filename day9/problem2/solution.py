n = int(input())
for i in range(0, n):
    for j in range(65 + i, 64, -1):
        a = chr(j)
        print(a, end=" ")
    print()
