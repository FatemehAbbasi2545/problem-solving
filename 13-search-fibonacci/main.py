
def fibo(n: int) -> list[int]:
    current, next = 0, 1; sequence = [current, next]
    for _ in range(2, n):
        current, next = next, current + next
        sequence.append(next)
    return sequence

def sequence_moify(sequence: list[int], m: int) -> list[int]:
    i = -1
    while True:
        if (sequence[i] > m):
            sequence.pop()
        else:
            break
    return sequence

def select(sequence: list[int], m: int) -> list[int] | None:
    index = len(sequence) - 1
    if sequence[index] <= m:
        return sequence       
    index = len(sequence) * 4 // 5
    if m > sequence[index]:
        return sequence_moify(sequence, m)
    if m == sequence[index]:
        return sequence[:index + 1]
    return select(sequence[:index + 1], m)

def main():
    try:
        n = int(input('Enter an integer number: '))
        m = int(input('Enter an positive integer number: '))
        if m <= 0:
            raise ValueError(999)
        sequence = select(fibo(n), m)
        print(f'Values ​​less than or equal to 100 in the Fibonacci sequence are: {sequence}')
    except ValueError as e:
        if e.args[0] == 999:
            print('The second input must be a positive integer.')
        else:
            print('Invalid number')

if __name__ == '__main__':
    main()