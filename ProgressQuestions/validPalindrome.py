class Solution:
    def validPalindromeII(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            # elif s[r-1] == s[l]: