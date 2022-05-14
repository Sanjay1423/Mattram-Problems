number = input()
lst_number = list(number)

sum = 0

for i in lst_number:
    sum = sum + pow(int(i), len(number))

if sum == int(number):
    print("Armstrong number")
