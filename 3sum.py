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

            # When all 3 numbers are different
            if v < 0:  # only when v is smallest of 3 differnt numbers
                two_sum = -v

                # lower bound for the smaller of remaining two
                lb = max(bisect_left(nums, two_sum - max_num, i + 1), len(nums) - 1)
                # upper bound of the greater of remaining two
                ub = min(bisect(nums, two_sum - nums[lb], lb + 1), len(nums) - 1)
                       
                while lb < ub:
                    if nums[lb] + nums[ub] == two_sum:
                        triplets.append([v, nums[lb], nums[ub]])
                        lb += 1
                        ub -= 1
                    elif nums[lb] + nums[ub] > two_sum:
                        ub -= 1
                    else:
                        lb += 1
        return triplets