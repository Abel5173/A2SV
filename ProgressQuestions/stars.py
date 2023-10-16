nums = [3,2,2,3]
val = 3
# for i in range(1, len(nums)):
#     if nums[i] == nums[i-1]:
#         nums.pop(i-1)

i = len(nums) - 1
for j in range(len(nums)):
    if nums[j] == val:
        nums[j], nums[i] = nums[i], nums[j]
        i -= 1
print(nums)