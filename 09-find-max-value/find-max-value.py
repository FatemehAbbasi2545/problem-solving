numbers = []
internal_list = []

attempts = 0
max_attempts = 3

for i in range(5):
    for j in range(8):
        while attempts <= max_attempts:
            try:
                user_input = int(input('Enter an integer number: '))
                internal_list.append(user_input)
                break
            except ValueError:
                attempts += 1
                print(f'Error: The entered value is not valid. There are {max_attempts - attempts} opportunities left.')             

    numbers.append(internal_list)
    print(f'Max value of row {i} is: {max(internal_list)}')
    internal_list = []

print(numbers)
