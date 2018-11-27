class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    map = {}
    for i, v in enumerate(nums):
        complement = target - v
        if complement in map:
            return [map[complement], i]
        map[v] = i