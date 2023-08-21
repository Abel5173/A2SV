class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict = {element: index for index, element in enumerate(nums)}
        for current_element, new_element in operations:
            index = dict[current_element]
            nums[index] = new_element
            del dict[current_element]
            dict[new_element] = index
        return nums

