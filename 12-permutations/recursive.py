import math

def find_all_permutations(letters: list[str]):
    n = len(letters)
    
    result = []
    stack = []
    used = {i: False for i in range(n)}

    def backtrack():
        if len(stack) == n:
            word = ''.join(stack)
            result.append(word)
            print(word)
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                stack.append(letters[i])
                backtrack()
                stack.pop()
                used[i] = False

    backtrack()
    return len(result)

def find_all_possible_combinations(letters: list[str], r: int):    
    n = len(letters); combinations = []; path = []
    used = [False] * len(letters)

    def backtrack(start):
        if len(path) == r:
            combinations.append(path.copy())
            return
        for i in range(start, n):
            if not used[i]:
                used[i] = True
                path.append(letters[i])
                backtrack(i + 1)
                path.pop()
                used[i] = False

    backtrack(0)
    return combinations

def main():
    letters = ['f','l','o','w','e','r']; n = len(letters); r = 4

    p = int(math.factorial(n) / math.factorial(n - r)) # Number of permutations of r objects out of n objects
    c = int(p / math.factorial(r)) # Number of combinations of r objects out of n objects

    combinations = find_all_possible_combinations(letters, 4)

    if (len(combinations) != c):
        print('The results produced are not correct.')
        return

    total_number = 0
    for c in combinations:
        total_number += find_all_permutations(c)

    if (total_number != p):
        print('The results produced are not correct.')

if __name__ == '__main__':
    main()