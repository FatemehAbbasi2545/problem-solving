value = 'A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression'

for i in range(8):
    output = ''
    for j in range(i, i + 8):
        output += value[j]
    print(output)