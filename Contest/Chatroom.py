l = input()
l = list(l)
a = 'hello'
j = 0
for i in a:
    isHello = False
    for j in range(len(l)):
        if i == l[j]:
            l = l[j+1:]
            isHello = True
            break
        
    if not isHello:
        break

print('YES' if isHello else 'NO')