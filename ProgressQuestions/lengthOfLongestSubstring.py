class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in checkSet:
                checkSet.remove(s[l])
                l += 1
            checkSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
# Code Explanation:
# The idea is to use a set to store the characters in the current window.
# We use set because it can check if a character is in the set in O(1) time.
# We use two pointers to maintain the window size.
# The right pointer is always moving forward.
# The left pointer only moves when there is a duplicate.
# We also use a variable to store the longest length of the substring.
# Time Complexity: O(n)
# Space Complexity: O(n)
