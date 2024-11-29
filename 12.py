from funcs import nS, extended_euclidean_algorithm, p_add_q
text = """Ведите h, d, k, h, Q, (r,s) в формате:
11
2
8
2
(596,433)
(3,10)"""
print(text)
ha = int(input())
d = int(input())
k = int(input())
hb = int(input())
Q = list(map(int, input()[1:-1].split(',')))
rs = list(map(int, input()[1:-1].split(',')))

a, b = -1, 1
GA = (416, 55)
GB = (562, 89)
n = 13
p = 751

print('Задание А')
kG = nS(k, *GA, p, a)
print(f'kG={k}{GA}={kG}')
r = kG[0] % n
print(f'{r=}')
gcd, xe, ye = extended_euclidean_algorithm(k, n)
z = xe % n
print(f'{z=}')
s = z*(ha+d*r) % n
print(f's = {z}*({ha}+{d}*{r}) mod {n} = {s}')
print(f'цифровая подпись сообщения ({r},{s}).')

print('Задание B')
rb, sb = rs
assert 0 < rb < n and 0 < sb < n
print(f'0 < {rb} < {n} and 0 < {sb} < {n}')
gcd, xe, ye = extended_euclidean_algorithm(sb, n)
v = xe % n
print(f'v = {xe} mod {n} = {v}')
u1 = hb*v%n
print(f'u1 = {hb}*{v} mod {n}')
u2 = rb*v%n
print(f'u2 = {rb}*{v} mod {n}')
X = p_add_q(*nS(u1, *GB, p, a), *nS(u2, *Q, p, a), p, a)
print(f'X = {u1}{GB}+{u2}{Q} = {X}')
assert rb == X[0]%n
print(f'{rb} == {X[0]} mod {n}')