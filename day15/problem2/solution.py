
# * O/P  => https://www.hackkerrank.com/domains/python/


# ! => ['www', 'hackkerrank', 'com', 'domains', 'python']
input = input().split('#')

string = f'https://{input[0]}.{input[1]}.{input[2]}/{input[3]}/{input[4]}/'
print(string)
