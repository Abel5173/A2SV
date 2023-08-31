n = int(input())
a = list(map(int, input().split()))
e, o = 0, 0

for i in a:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
if e != 0 and o != 0:
    a.sort()
    print(*a)
else:
    print(*a)