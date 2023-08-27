n,k = map(int, input().split())
for i in range(n):
    a = int(input())
    while k > 0:
        if a % 2 == 0:
            a = a//2
            k -= 1
        else:
            break
        
if k == 0:
    print(1)
else:
    print(0)