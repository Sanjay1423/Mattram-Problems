word = input()
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
consonants = ['b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S'
              't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

if word in vowels:
    print("Vowel")
elif word in consonants:
    print("Consonant")
else:
    print("Not an alphabet")
