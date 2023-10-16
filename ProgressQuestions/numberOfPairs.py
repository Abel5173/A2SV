n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l, r = 0, 0
cnt = 0
temp = 0
while l < n and r < m:
    if l1[l] == l2[r]:
        cnt += 1
        temp += 1
        l += 1
    elif l1[l] > l2[r]:
        r += 1
        if r > 0 and r < m and l2[r] == l2[r-1]:
            cnt += temp
        else:
            temp = 0
    else:
        l += 1

print(cnt)
