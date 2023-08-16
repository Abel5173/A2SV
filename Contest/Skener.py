r, c, zr, zc = map(int, input().split())
mat = []
for i in range(r):
    s = input()
    mod = ''
    for j in s:
        mod += j*zc
    for j in range(zr):
        mat.append(mod) 
for i in mat:
    print(i)