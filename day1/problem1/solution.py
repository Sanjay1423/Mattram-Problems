string = input()
str_list = list(string)
vowels = ['a', 'A', 'e', "E", 'i', 'I', 'o', 'O', 'u', 'U']
for i in str_list:
    if i in vowels:
        str_list.remove(i)

print(''.join(str_list))
