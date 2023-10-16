nums = [0,-1,-1,-1,-1,-1]
for i in range(1, len(nums)):
    nums[i] = nums[i] + nums[i-1]
for i in range(len(nums)):
    if nums[-1] - nums[i] == nums[i-1]:
        print(i)
    if i == 0 and nums[-1] - nums[i] == 0:
        print(0)
    if i == len(nums) -1 and nums[i-1] == 0:
        print(0)
