import math

r = int(input())
if r == 1:
    print(1, 1)
    exit()
for x in range(1, r):
    if math.sqrt((r**2 + 1)-x**2).is_integer():
        print(x, int(math.sqrt((r**2 + 1)-x**2)))
        break