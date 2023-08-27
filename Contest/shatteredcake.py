W = int(input())
n = int(input())
total_area = 0
for _ in range(n):
    wi, li = map(int, input().split())
    total_area += wi * li

print(total_area // W)