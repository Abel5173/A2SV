from bisect import bisect_right

def interestingdrink(day, prices, n):
    return bisect_right(prices, day)
    

n = int(input())
prices = list(map(int, input().split()))
q = int(input())
days = [int(input()) for i in range(q)]
prices.sort()
for i in days:
    print(interestingdrink(i, prices, n))