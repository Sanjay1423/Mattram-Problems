number = input()
lst_number = list(number)
lst_number.reverse()
str_number = ''.join(lst_number)

if int(number) == int(str_number):
    print(f'{number} is a palindrome')
else:
    print(f'{number} is a not a palindrome')
