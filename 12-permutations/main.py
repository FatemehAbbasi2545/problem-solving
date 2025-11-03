import math
import random

def find_all_permutations(letters: list[str]):
    n = len(letters); permutations = []

    p = int(math.factorial(n) / math.factorial(n - n)) # Number of permutations of r objects out of n objects

    while True:
        result = []
        first_letter = random.choice(letters)
        result.append(first_letter)
        while True:
            next_letter = random.choice(letters)
            if next_letter not in result:
                result.append(next_letter)
            if len(result) == n:
                word = ''.join(result)
                if word not in permutations:
                    permutations.append(word)
                    print(word)
                break
        if len(permutations) == p:
            break
    
    return len(permutations)

def find_all_possible_combinations(letters: list[str], r: int):    
    n = len(letters); combinations = []

    for i1 in range(n - r + 1):        
        for i2 in range(i1 + 1, n - r + 2):
            for i3 in range(i2 + 1, n - r + 3):
                for i4 in range(i3 + 1, n):
                    combinations.append([letters[i1], letters[i2], letters[i3], letters[i4]])

    return combinations

def main():
    letters = ['f','l','o','w','e','r']; n = len(letters); r = 4

    p = int(math.factorial(n) / math.factorial(n - r)) # Number of permutations of r objects out of n objects
    c = int(p / math.factorial(r)) # Number of combinations of r objects out of n objects

    combinations = find_all_possible_combinations(letters, r)

    if (len(combinations) != c):
        print('The results produced are not correct.')
        return

    total_number = 0
    for c in combinations:
        total_number += find_all_permutations(c)

    if (total_number != p):
        print('The results produced are not correct.')
    else: print(total_number)

if __name__ == '__main__':
    main()