# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
# candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique 
# if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that 
# sum up to target is less than 150 combinations for the given input.
# How to solve:
# 1. Sort the array
# 2. Use a recursive function to find the combinations
# 3. If the sum of the combination is greater than the target, return
# 4. If the sum of the combination is equal to the target, add the combination to the result
# 5. If the sum of the combination is less than the target, call the recursive function again with the same array and the sum
# 6. In the recursive function, use a for loop to iterate through the array
# 7. In the for loop, append the current element to the combination and call the recursive function again with the same array and the sum minus the current element
# 8. In the for loop, pop the last element from the combination
# 9. In the recursive function, use a for loop to iterate through the array
# 10. In the for loop, append the current element to the combination and call the recursive function again with the same array and the sum minus the current element
# 11. In the for loop, pop the last element from the combination
# 12. Return the result
# Time Complexity: O(2^n)
# Space Complexity: O(n)

