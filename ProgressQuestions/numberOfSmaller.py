n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

ans = []
l, r = 0, 0 
count = 0
while r < m:
    while l < n and l2[r] > l1[l]:
        count += 1
        l += 1
    ans.append(count)
    r += 1

print(*ans)
