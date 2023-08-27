s = input()
l = len(s)//3
m = []
for i in range(0, len(s), l):
    m.append(s[i:i+l])
if m[0] == m[1]:
    print(m[0])
elif m[0] == m[2]:
    print(m[0])
else:
    print(m[1])
