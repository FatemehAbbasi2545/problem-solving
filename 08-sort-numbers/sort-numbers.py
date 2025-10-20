
numbers = []
result = []

for i in range(10):
    try:
        input_value = int(input('Enter a number: '))        
    except ValueError:
        print('Error: The input value is not valid.')
    else:
        numbers.append(input_value)

while len(numbers) > 0:
    min_value = min(numbers)
    result.append(min_value)
    numbers.remove(min_value)

print(result)
