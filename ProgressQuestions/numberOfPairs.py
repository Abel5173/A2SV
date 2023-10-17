n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
pairs = 0
dic = {}
for i in l1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in l2:
    if i in dic:
        pairs += dic[i]
print(pairs)
