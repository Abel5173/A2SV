class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        s = set(nums)
        s_len = len(s)
        ans = list(s)
        for i in range(length - s_len):
            ans.append('_')
        return s_len, ans
    #  5, nums = [0,1,2,3,4,_,_,_,_,_]