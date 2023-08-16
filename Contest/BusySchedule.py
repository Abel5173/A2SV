def sortTime(ts):
    hm, z = ts.split()
    h, m = map(int, hm.split(':'))
    if z == 'a.m.' and h == 12:
        h = 0
    elif z == 'p.m.' and h != 12:
        h += 12
    return h*60 + m

while True:
    t = int(input())
    if t == 0:
        break
    ts = []
    for _ in range(t):
        ts.append(input())

    ts.sort(key=sortTime)
    for i in ts:
        print(i)
    print()