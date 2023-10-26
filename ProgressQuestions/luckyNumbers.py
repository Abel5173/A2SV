t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    max_num = int(str(l)[0]) - int(str(l)[-1])
    m = l
    for i in range(l, min(l+101, r+1)):
        n = sorted(list(str(i)))
        if int(n[-1]) - int(n[0]) > max_num:
            max_num = int(n[-1]) - int(n[0])
            m = i
        if max_num == 9:
            break
    print(m)