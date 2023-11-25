class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""
        l, r = 0, 0
        while l < len(word1) and r < len(word2):
            newWord += word1[l] + word2[r]
            l, r = l + 1, r + 1
        newWord += word2[r:] if l == len(word1) else word1[l:]
        return newWord
