def get_inpu_data() -> list[int]:
    numbers = []
    for i in range(10):
        try:
            input_value = int(input('Enter a number: '))        
        except ValueError:
            print('Error: The input value is not valid.')
        else:
            numbers.append(input_value)

    return numbers

def sort(numbers: list[int]) -> list[int]:
    result = []
    while len(numbers) > 0:
        min_value = min(numbers)
        result.append(min_value)
        numbers.remove(min_value)

    return result

def main():
    numbers = get_inpu_data()
    result = sort(numbers)
    print(result)

if __name__ == "__main__":
    main()
