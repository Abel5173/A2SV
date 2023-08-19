class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            cnt = 0
            for j in nums:
                if i > j:
                    cnt += 1
            l.append(cnt)
        return l