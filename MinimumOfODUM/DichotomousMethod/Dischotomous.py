# CONDITION VARIABLES
a = 0
b = 21
delta = 0.1

# NON CONDITION VARIABLES
ar = a
br = b
epsilon = 1

Fx1 = 1000000
Fx2 = 0
i = 1


# CONDITION FUNCTION
def function(x):
    return 2 * (x + 3)**2 + 3

if __name__ == '__main__':
    print(f'xr0 = (ar + br) / 2')
    print(f'xr1 = (xr0 - delta) / 2')
    print(f'xr2 = (xr0 + delta) / 2')

    print(f'ТИН1 = [{ar}, {br}]')

    while ((br - ar) > epsilon):
        xr0 = round((ar + br) / 2, 3)
        xr1 = round(xr0 - delta / 2, 3)
        xr2 = round(xr0 + delta / 2, 3)

        print(f'xr0 = {xr0} \nxr1 = {xr1} \nxr2 = {xr2}')

        Fx1, Fx2 = round(function(xr1), 3), round(function(xr2), 3)

        if Fx1 != Fx2:
            print(f'Ф(x1^{i}) = {Fx1} \nФ(x2^{i}) = {Fx2}')
        else:
            print(f'Ф(x1^{i}) = Ф(x2^{i}) = {Fx1}')

        if Fx1 < Fx2:
            print(f'Ф(x2^{i}) > Ф(x1^{i})')
            br = xr2
        elif Fx1 == Fx2:
            print(f'Ф(x1^{i}) = Ф(x2^{i})')
            ar = xr1
        else:
            print(f'Ф(x1^{i}) > Ф(x2^{i})')
            ar = xr1

        i += 1

        print(f'\nТИН{i} = [{ar}, {br}]')
