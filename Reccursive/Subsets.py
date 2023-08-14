# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# how to solve:
# 1. Sort the array
# 2. Use a recursive function to find the subsets
# 3. In the recursive function, use a for loop to iterate through the array
# 4. In the for loop, append the current element to the subset and call the recursive function again with the same array
# 5. In the for loop, pop the last element from the subset
# 6. In the recursive function, use a for loop to iterate through the array
# 7. In the for loop, append the current element to the subset and call the recursive function again with the same array
# 8. In the for loop, pop the last element from the subset
# 9. Return the result
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Python code:

def subsets(nums):
    nums.sort()
    result = []
    subsetsHelper(nums, [], result)
    return result

def subsetsHelper(nums, subset, result):
    result.append(subset[:])
    for i in range(len(nums)):
        subset.append(nums[i])
        subsetsHelper(nums[i + 1:], subset, result)
        subset.pop()
    return
# sample execution example
# Input: nums = [1,2,3]
# Output: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
# Explanation: The solution set must not contain duplicate subsets.
nums = [1,2,3]
print(subsets(nums))