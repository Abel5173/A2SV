class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        cnt = 0
        for i in range(2, len(prime)):
            if i == n and prime[n]:
                return cnt
            elif prime[i]:
                cnt += 1
        return cnt
