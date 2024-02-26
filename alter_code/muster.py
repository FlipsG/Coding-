def dreieck_muster():
    for i in range(1, 7):
        print('x' * i)

    for i in range(5, 0, -1):
        print('x' * i)

dreieck_muster()

def kompliziertes_muster(n):
    for i in range(1, n * 2):
        if i <= n:
            spaces = ' ' * (n - i)
            print(f'{spaces}{"x" * i}{"y" * (2 * i - 2)}')
        else:
            spaces = ' ' * (i - n)
            print(f'{spaces}{"x" * (n * 2 - i)}{"y" * (2 * (n * 2 - i) - 2)}')

kompliziertes_muster(6)