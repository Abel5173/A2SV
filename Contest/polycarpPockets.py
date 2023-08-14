n = int(input())
a = list(map(int, input().split()))
max = 0
for i in a:
    if a.count(i) > max:
        max = a.count(i)
print(max)

        