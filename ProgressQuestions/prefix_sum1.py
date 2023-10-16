n = int(input())
l = list(map(int, input().split()))

prefix_sum = [0] * (len(l)+1)
for i in range(1, len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + l[i-1]

print(*prefix_sum)