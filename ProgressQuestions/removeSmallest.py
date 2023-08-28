t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 1
    while i < len(a) and len(a) > 1:
        if a[i] - a[i-1] == 1:
            min_ = min(a[i], a[i-1])
            a.pop(a.index(min_))
            i -= 1
        elif a[i] - a[i-1] == 0:
            a.pop(i-1)
            i -= 1
        i += 1
    print('YES' if len(a) == 1 else 'NO')