class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        s = sum([j for j in nums if j % 2 == 0])
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0:
                nums[queries[i][1]] -= queries[i][0]
                s -= nums[queries[i][1]]
            else:
                nums[queries[i][1]] += queries[i][0]
                s += queries[i][0]
            ans.append(s)
        return ans