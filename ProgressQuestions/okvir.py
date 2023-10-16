n, m = map(int, input().split())
u, l, r, d = map(int, input().split())
li = []
k = []
for i in range(n):
    a = input()
    for j in a:
        k.append(j)
c = '#'
for i in range(n+u+d):
    v = []
    for j in range(m+l+r):
        if i == 0:
            v.append(c)
            c = '.' if c == '#' else '#'
        else:
            c = '.' if li[i-1][j] == '#' else '#' 
            v.append(c)
    li.append(v)
x = 0         
for i in range(u,n+u):
    for j in range(l,m+l):
        li[i][j] = k[x]
        x += 1
for i in li:
    for j in i:
        print(j,end='')
    print()