def mariasStones(q, stones, n):
    q2 = stones.copy()
    q2.sort()
    if q[0] == 1:
        return sum(stones[q[1]-1:q[2]])
    else:
         return sum(q2[q[1]-1:q[2]])
    
    return 0
n = int(input())
stones = list(map(int, input().split()))
m = int(input())
q = [(list(map(int, input().split()))) for i in range(m)]

for i in q:
    print(mariasStones(i, stones, n))