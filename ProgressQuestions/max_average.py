nums = [4,2,1,3,3]
k = 2

sm = sum(nums[:k])
max_avg = sm / k
i = 1
while i+k <= len(nums):
    sm += nums[i+k-1] - nums[i-1]
    if max_avg < (sm / k):
        max_avg = sm / k
    i += 1
print(max_avg) 