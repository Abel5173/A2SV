n = int(input())
arr = list(map(int, input().split()))
q = int(input())

# prefix_sum = [0] * (len(arr))
# prefix_sum[0] = arr[0]
for i in range(1, len(arr)):
    arr[i] = arr[i-1] + arr[i]
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l == r:
        print(arr[l])
    else:
        print(arr[r]-arr[l-1])
# print(*prefix_sum)