input = input()

if "http://www." in input:
    print(input.replace('http://www.', ''))
elif "https://www." in input:
    print(input.replace('https://www.', ''))
