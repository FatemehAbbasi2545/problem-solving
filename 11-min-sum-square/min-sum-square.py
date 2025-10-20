
def min_sum_square(a: list):
    n = len(a)
    result = [] 
    for i in range(n):
        for j in range(i , n):
            s = a[i] + a[j]
            x = s ** 2
            result.append(x)
    return min(result)

def min_sum_square_bruteforce(a: list):
    n = len(a)
    best = float('inf')  
    for i in range(n):
        for j in range(i , n):
            s = a[i] + a[j]
            x = s * s
            if x < best:
                best = x
    return best

# Quick version with two pointers after sorting
def min_sum_square_two_pointers(a):
    a.sort()
    i = 0
    j = len(a) - 1
    best = float('inf')
    while i <= j:
        s = a[i] + a[j]
        if s * s < best:
            best = s * s
        if s > 0:
            j -= 1
        elif s < 0:
            i += 1
        else:
            return 0
    return best

def main():
    a = list((-3, 1, 4, -1, 2))

    min_value = min_sum_square(a)
    print(min_value)

    min_value = min_sum_square_bruteforce(a)
    print(min_value)

    min_value = min_sum_square_two_pointers(a)
    print(min_value)

if __name__ == "__main__":
    main()