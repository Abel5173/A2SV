class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        maxLen = 0
        preS = "="

        for r in range(len(arr)):
            if r == 0:
                maxLen = 1
                continue

            if arr[r - 1] < arr[r] and preS != "<":
                preS = "<"
                maxLen = max(maxLen, r - l + 1)
            elif arr[r - 1] > arr[r] and preS != ">":
                preS = ">"
                maxLen = max(maxLen, r - l + 1)
            elif arr[r - 1] == arr[r]:
                l = r
                preS = "="
            else:
                l = r - 1
        
        return maxLen

