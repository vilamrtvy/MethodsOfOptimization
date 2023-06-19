# CONDITION VARIABLES
a = 0
b = 13
delta = 0.1
N = 6


# CONDITION FUNCTION
def function(x):
    return 2 * (x - 12)**2 + 3


def iteration_cycle(x1, x2, k_it):
    f_x1 = function(x1)
    f_x2 = function(x2)

    if f_x1 != f_x2:
        print(f'Ф(x1^{k_it+1}) = {f_x1}')
        print(f'Ф(x2^{k_it+1}) = {f_x2}')
    else:
        print(f'Ф(x1^{k_it+1}) = Ф(x2^{k_it+1}) = {f_x1}')

    if f_x1 < f_x2 or f_x1 == f_x2:
        if f_x1 < f_x2:
            print(f'Ф(x2^{k_it+1}) > Ф(x1^{k_it+1})')
        else:
            print(f'Ф(x1^{k+1}) = Ф(x2^{k_it+1})')
        return True
    else:
        print(f'Ф(x1^{k+1}) > Ф(x2^{k_it+1})')
        return False


def fibonacci(index):
    if index in (0, 1):
        return 1

    fn1, fn2 = 1, 1
    for it in range(2, index + 1):
        fn1, fn2 = fn2, fn1 + fn2
    return fn2


def conditionCheck(x1, x2, a, b, i, condition):
    if i == N:
        if condition is False:
            print('ТИН = [', x1, ',', b, ']')
        else:
            print('ТИН = [', a, ',', x1, ']')
    elif i != N - 1:
        if condition is True:
            b, x2, x1 = x2, x1, a + (fibonacci(N - k - 3) / fibonacci(N - k - 1)) * (x2 - a)
        else:
            a, x1, x2 = x1, x2, x1 + (fibonacci(N - k - 2) / fibonacci(N - k - 1)) * (b - x1)
    return x1, x2, a, b


if __name__ == '__main__':
    a, b, = a, b
    k, x1, x2, = 0, 0, 0

    print(f'x1 = a + (Fn-2 / Fn) * (b - a)')
    print(f'x2 = a + (Fn-1 / Fn) * (b - a)')

    for i in range(0, N):
        print(f'\nШАГ {i+1}')
        print(f'ТИН{i+1} = [{a}, {b}]')

        if i == 0:
            fn1, fn2 = fibonacci(N - 1), fibonacci(N - 2)
            fn = fn1 + fn2
            x1, x2 = a + (fn2 / fn) * (b - a), a + (fn1 / fn) * (b - a)

        if i == N - 1:
            print(f'x1^{i + 1} = x_1^{i} = {x1}')
            x2 += delta
            print(f'x2^{i + 1} = x_1^{i} + {delta} = {x2}')
        else:
            print(f'x1^{i + 1} = {x1}')
            print(f'x2^{i + 1} = {x2}')

        x1, x2, a, b = conditionCheck(x1, x2, a, b, i, iteration_cycle(x1, x2, k))
        k += 1
