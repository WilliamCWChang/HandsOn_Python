#Tower of Hanoi
count = 0
def hanoi(n, start='A', buffer='B', end='C'): 
    if n == 1:
        print('move', start, '-->', end)
        return

    hanoi(n-1, start, end, buffer) 
    print('move', start, '-->', end)
    hanoi(n-1, buffer, start, end)

print(hanoi(5))
