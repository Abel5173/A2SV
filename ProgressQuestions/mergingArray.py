n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

k = (n+m-1)
arr = [0]*(n+m)
l, r = n-1, m-1
while l > -1 and r > -1:
    if l1[l] > l2[r]:
        arr[k] = l1[l]
        l -= 1
    else:
        arr[k] = l2[r]
        r -= 1
    k -= 1
if l >= 0:
    arr[:k+1] = l1[:l+1]
else:
    arr[:k+1] = l2[:r+1]

print(*arr)
