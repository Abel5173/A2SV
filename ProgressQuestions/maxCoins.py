class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        cnt = 0
        while piles:
            cnt += piles[-2]
            piles.pop()
            piles.pop()
            piles.pop(0)
        return cnt