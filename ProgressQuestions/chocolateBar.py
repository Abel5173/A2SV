n = int(input())
times = list(map(int, input().split()))

aliceSpend, bobSpend = 0, 0
aliceCnt, bobCnt = 0, 0
i, j = 0, n-1

while(i <= j):
    if aliceSpend <= bobSpend:
        aliceSpend += times[i]
        aliceCnt += 1
        i += 1
    else:
        bobSpend += times[j]
        bobCnt += 1
        j -= 1
print(aliceCnt, bobCnt)