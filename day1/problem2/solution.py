n = int(input())
arr = [int(i) for i in input().split()]
sum = 0
prod = 1

for i in arr:
    sum += i
    prod *= i

if sum % 2 == 0:
    print(sum)
else:
    print(prod)


