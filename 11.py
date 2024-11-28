from funcs import p2, p_add_q, negR, nS
import pandas as pd

print('введите Pb, X, k, ab, Y в формате',
      """
(188,93)
отступить
7, 9, 3, 8, 18, 18, 8, 11, 16
25
{(425,663), (651,191)}; {(188,93), (177,562)}; {(286,136), (603,562)}; {(440,539), (588,707)}; {(72,254), (269,187)}; {(56,419), (49,568)}; {(16,416), (426,662)}; {(425,663), (557,28)}; {(188,93), (149,97)}; {(179,275), (711,341)}
""", sep='\n'
      )
Pb = tuple(map(int, input()[1:-1].split(',')))
X = input()
K = map(int, input().split(', '))
ab = int(input())
Ystr = input()

Y = []
a, b = -1, 1
p = 751
GA = (0, 1)
GB = (-1, 1)

for cord in Ystr.split('; '):
    x, y = cord[1:-1].split(', ')
    x = map(int, x[1:-1].split(','))
    y = map(int, y[1:-1].split(','))
    Y.append((tuple(x), tuple(y)))
chars2point = pd.read_csv('symbols.csv', dtype={'char': str, 'point': str})
# Применяем split и распаковываем результат в два столбца
chars2point[['x', 'y']] = chars2point['point'].str.extract(r'\((\d+),\s*(\d+)\)')

# Преобразуем x и y в числовой формат, если нужно
chars2point['x'] = chars2point['x'].astype(int)
chars2point['y'] = chars2point['y'].astype(int)

print('Задание A')
Ycript = []
for k, char in zip(K, X):
    Pm = chars2point[chars2point['char'] == char][['x', 'y']].values[0]
    kG = nS(k, *GA, p, a)
    kPb = nS(k, *Pb, p, a)
    Pm_add_kPb = p_add_q(*Pm, *kPb, p, a)
    Ycript.append((kG, Pm_add_kPb))
    print(f'{char}->{Pm}')
    print(f'Y=({k}{GA}, {Pm}+{k}{Pb}')
print('Шифр -', Ycript)

print('Задание B')
chars = []
for x_cord, y_cord in Y:
    abkG = nS(ab, *x_cord, p, a)
    neg_abkG = negR(*abkG, p)
    point = p_add_q(*y_cord, *neg_abkG, p, a)
    char = chars2point[(chars2point['x'] == point[0]) & (chars2point['y'] == point[1])]['char'].values[0]
    chars.append(char)
    print(f'{x_cord}-{ab}{y_cord}={point}->{char}')
print(''.join(chars))
