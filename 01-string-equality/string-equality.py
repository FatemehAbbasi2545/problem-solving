first_str = input('Enter a text: ')
second_str = input('Enter a text: ')

first_dict = {}
for c in first_str:
    first_dict[c] = first_dict.setdefault(c, 0) + 1

second_dict = {}
for c in second_str:
    second_dict[c] = second_dict.setdefault(c, 0) + 1

print(first_dict == second_dict)

