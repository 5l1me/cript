from fractions import Fraction


def extended_euclidean_algorithm(a, b):
    """
    Возвращает кортеж из трёх элементов (gcd, x, y), такой, что
    a * x + b * y == gcd, где gcd - наибольший
    общий делитель a и b.

    В этой функции реализуется расширенный алгоритм
    Евклида и в худшем случае она выполняется O(log b).
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def p2(x, y, p, a, z=None):
    """
    Функция принимает координаты точки P,
    значения p, a
    возвращает координаты 2P
    """
    if z is not None:
        print(f'считаем {z}')
        print(f'p2({x=}, {y=}, {p=}, {a=})')
    if 3 * x ** 2 + a % 2 * y != 0:
        f = Fraction(3 * x ** 2 + a, 2 * y)  # Вычисление значения натуральной дроби по модулю
        gcd, xe, ye = extended_euclidean_algorithm(f.denominator, p)  # с помощью расширенного алгоритма Евклида
        lamb = f.numerator * xe % p
        if z is not None:
            print(f'lamb={f.numerator}*{xe}mod{p}={lamb}')
    else:
        lamb = (3 * x ** 2 + a) // (2 * y) % p
        if z is not None:
            print(f'lamb={3 * x ** 2 + a}/{2 * y}mod{p}={lamb}')
    x3 = (lamb ** 2 - 2 * x) % p  # находим x3
    if z is not None:
        print(f'x3={lamb ** 2 - 2 * x}mod{p}={x3}')
    y3 = (-y + lamb * (x - x3)) % p  # находим y3
    if z is not None:
        print(f'y3={-y + lamb * (x - x3)}mod{p}={y3}')
        print(f'проверяем принадлежность кривой\n{y3 ** 2}mod{p}==({x3 ** 3}+{a * x3}+1)mod{p}')
        print(f'{y3 ** 2 % p}=={(x3 ** 3 + a * x3 + 1) % p}\n')
    assert y3 ** 2 % p == (x3 ** 3 + a * x3 + 1) % p  # вызываем ошибку если точка не принадлежит кривой
    return x3, y3


def p_add_q(x1, y1, x2, y2, p, a, z=None):
    """
    Функция принимает координаты точки P и Q,
    значения p, a
    возвращает координаты P+Q
    """
    if z is not None:
        print(f'считаем {z}')
        print(f'p_add_q({x1=}, {y1=}, {x2=}, {y2=}, {p=}, {a=})')
    if (x1, y1) == (x2, y2):
        return p2(x1, y1, p, a, z)
    if (y2 - y1) % (x2 - x1) != 0:
        f = Fraction((y2 - y1), (x2 - x1))  # Вычисление значения натуральной дроби по модулю
        gcd, xe, ye = extended_euclidean_algorithm(f.denominator, p)  # с помощью расширенного алгоритма Евклида
        lamb = f.numerator * xe % p
        if z is not None:
            print(f'lamb={f.numerator}*{xe}mod{p}={lamb}')
    else:
        lamb = (y2 - y1) // (x2 - x1) % p
        if z is not None:
            print(f'lamb={y2 - y1}/{x2 - x1}mod{p}={lamb}')
    x3 = (lamb ** 2 - x1 - x2) % p  # находим x3
    if z is not None:
        print(f'x3={lamb ** 2 - x1 - x2}mod{p}={x3}')
    y3 = (-y1 + lamb * (x1 - x3)) % p  # находим y3
    if z is not None:
        print(f'y3={-y1 + lamb * (x1 - x3)}mod{p}={y3}')
        print(f'проверяем принадлежность кривой\n{y3 ** 2}mod{p}==({x3 ** 3}+{a * x3}+1)mod{p}')
        print(f'{y3 ** 2 % p}=={(x3 ** 3 + a * x3 + 1) % p}\n')
    assert y3 ** 2 % p == (x3 ** 3 + a * x3 + 1) % p  # вызываем ошибку если точка не принадлежит кривой
    return x3, y3


def negR(x, y, p, z=None):
    """
    Функция принимает координаты точки R,
    значения p, a
    возвращает координаты -R
    """
    if z is not None:
        print(f'считаем {z}')
        print(f'{x=} y={-y}mod{p}={-y % p}\n')
    return x, -y % p


def nS(n, xS, yS, p, a, z=None):
    """
    Функция принимает n, координаты S,
    значения p, a
    возвращает координаты nS
    """
    if z is not None:
        print(f'считаем {n}{z}')
    now = (xS, yS)
    decay = bin(n)[2:]  # находим разложение числа n с помощью двоичного представления
    z_desc = z  # сохраняем формулу разложения в строке
    for i in range(1, len(decay)):
        if decay[i] == '1':
            z_desc = f'{z}+2({z_desc})'
            now = p_add_q(xS, yS, *p2(*now, p, a, z=z_desc[2:] if z else None), p, a, z=z_desc if z else None)
        else:
            z_desc = f'2({z_desc})'
            now = p2(*now, p, a, z=z_desc if z else None)
    if z is not None:
        print(f'{n}{z} =', z_desc)
    return now
