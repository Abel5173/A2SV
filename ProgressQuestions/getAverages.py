nums = [7,4,3,9,1,8,5,2,6]
def getAverages(nums, k):
        if k > len(nums):
            return [-1]
        # if k == 0:
        #     return [nums[0]]
        avgs = [-1]*len(nums)
        i = k
        sm = sum(nums[i-k:i+k])
        while k + i < len(nums):
            sm += nums[i+k]
            avgs[i] = sm // (2*k + 1)
            sm -= nums[i-k]
            i += 1
        return avgs
print(len(nums))
print(getAverages(nums, 3))
# print(sum(nums[0:2*3 + 1]))