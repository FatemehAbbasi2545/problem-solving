
user_input = input('Enter a text: ')

i = 0
output = ''

while i < len(user_input):
    j = 1
    count = 1
    while i + j < len(user_input) and user_input[i] == user_input[i + j]:
        count += 1        
        j += 1

    output += f'{user_input[i]}{count}' if count > 1 else f'{user_input[i]}'
    i = i + j

print(output)
