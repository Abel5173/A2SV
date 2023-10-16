n = 22
l = 0
r = n
mid=n
while True:
    op = input()
    if op == '<':
        mid = l + (r - l) // 2 
        r = mid + 1
        print(mid)
    elif op == '>':
        mid =( (r - l) // 2)
        l = mid - 1
        print(mid) 
    elif op == '=':
        print('!'+str(mid))
