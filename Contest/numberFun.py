t = int(input())
for _ in range(t):
    x,  y, n = map(int, input().split())
    if x + y == n:
        print('Possible')
    elif x - y == n or y - x == n:
        print('Possible')
    elif x * y == n:
        print('Possible')
    elif x / y == n or y / x == n:
        print('Possible')
    else:
        print('Impossible')