from funcs import p2, p_add_q, negR, nS

print('введите p, a, b, P, Q, R, S, n в формате',
      """
751
-1 1
59 365
59 386
105 382
53 474
120
""", sep='\n'
      )
p = int(input())
a, b = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
S = list(map(int, input().split()))
n = int(input())


print('вычисление задания A')
P2 = p2(*P, p, a, z='2P')
Q3 = p_add_q(*Q, *p2(*Q, p, a, z='2Q'), p, a, z='3Q')
print(
    '2P+3Q–R =',
    p_add_q(
        *p_add_q(*P2, *Q3, p, a, z='2P+3Q'),
        *negR(*R, p, z='-R'),
        p, a, z='2P+3Q–R'
    )
)


print('\n\nВычисления задания B')
print('nS =', nS(n, *S, p, a, z='S'))