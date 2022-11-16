
input = set(input())  # ! => {'v', 'e', 'w', 'i', 't', 'r', 'n'}
string = ""

for i in range(97, 123):     # ! chr(97) = 'a' , chr(98) = "b" ... chr(122) = 'z'
    if chr(i) not in input:
        string += chr(i)


print(string)
