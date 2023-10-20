class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        merge = []
        while l < len(word1) or r < len(word2):
            if word1[l:] >= word2[r:]:
                merge.append(word1[l])
                l += 1
            else:
                merge.append(word2[r])
                r += 1

        return ''.join(merge)