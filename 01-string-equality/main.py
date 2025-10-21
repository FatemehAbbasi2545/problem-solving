
def check_string_equality(first_str: str, second_str: str) -> bool:
    first_dict = {}
    for c in first_str:
        first_dict[c] = first_dict.setdefault(c, 0) + 1

    second_dict = {}
    for c in second_str:
        second_dict[c] = second_dict.setdefault(c, 0) + 1

    return first_dict == second_dict

def main():
    first_str = input('Enter a text: ')
    second_str = input('Enter a text: ')
    result = check_string_equality(first_str, second_str)
    print(result)

if __name__ == "__main__":
    main()