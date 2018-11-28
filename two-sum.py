class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # https://leetcode.com/articles/two-sum/#approach-3-one-pass-hash-table
        indices = {}  # number (key) and its index (value)
        for i, v in enumerate(nums):
            complement = target - v
            if complement in indices:
                return [indices[complement], i]
            indices[v] = i