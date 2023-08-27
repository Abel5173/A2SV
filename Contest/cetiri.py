a, b, c = map(int, input().split()) 
l = [a, b, c]
l.sort()
if l[1] - l[0] == l[2] - l[1]:
    print(l[2] + l[2] - l[1])
elif l[1] - l[0] > l[2] - l[1]:
    print(l[2] - l[1] + l[0])
elif l[1] - l[0] < l[2] - l[1]:
    print(l[1] - l[0] + l[1])
else:
    print(l[2] - l[1] + l[1])

    # 1, 4, 10