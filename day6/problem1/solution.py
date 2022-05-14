string = input()
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
sum = 0
for i in string:
    if i in vowels:
        sum += 1

print(sum)
