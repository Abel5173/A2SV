class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        cnt = 0
        while l < r:
            if nums[l] + nums[r] == k:
                cnt += 1
                r -= 1
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return cnt