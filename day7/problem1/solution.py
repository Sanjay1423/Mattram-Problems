from audioop import mul


n1 = int(input())
arr = map(int, input().split())
n2 = int(input())

multi_arr = list(map(lambda x: x*n2, arr))
multi_arr.sort(reverse=True)

for i in multi_arr:
    print(i, end=' ')
