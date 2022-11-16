
input = input()[:-2]  # ! => 2-3-4
input_list = input.split('-')  # ! => ['2', '3', '4']
output_list = []
output_string = "["
for i in range(1, int(input_list[-1])+1):
    if str(i) in input_list:
        output_string += '"Push",'
    else:
        output_string += '"Push","Pop",'

print(input, input_list)
print(output_string[:-1]+']')
