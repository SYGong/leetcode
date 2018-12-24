from collections import Counter
from bisect import bisect, bisect_left

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        if len(nums) < 3:
            return triplets
        num_freq = Counter(nums)
        nums = sorted(num_freq)  # sorted unique numbers
        
        # Get rid of numbers that are too large/small
        # such that no other number able to complete
        nums = nums[bisect_left(nums, -2 * nums[-1]) :
                    bisect(nums, -2 * nums[0])]
        if len(nums) < 1:
            return triplets

        max_num = nums[-1]
        for i, v in enumerate(nums):
            if num_freq[v] >= 2:
                complement =  -2 * v
                if complement in num_freq:
                    if complement != v or num_freq[v] >= 3:
                        triplets.append([v] * 2 + [complement])
            if v < 0:
                two_sum = -v
                lb = bisect_left(nums, two_sum - max_num, i + 1)
                ub = bisect(nums, two_sum // 2, lb)
                # lower/up bound        
                for u in nums[lb : ub]:
                    complement = two_sum - u
                    if complement in num_freq and u != complement:
                        triplets.append([v, u, complement])
        return triplets