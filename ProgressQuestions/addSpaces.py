class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        lastIndx = 0
        for i in spaces:
            ans += s[lastIndx:i]
            ans += ' '
            lastIndx = i
        ans += s[lastIndx:]
        return ans