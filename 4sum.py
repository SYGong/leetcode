from bisect import bisect_left
from collections import Counter

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum_pairs = {}
        N = 4
        quadruplets = []
        if len(nums) < N:
            return quadruplets
        nums = sorted(nums)

        for i, v in enumerate(nums):
            if i >= 1 and v != nums[i - 1]:
                for j, w in enumerate(nums[1+1:]):
                    if w != nums[j - 1]:
                        sum_ = v + w
                        sum_pairs.setdefault(sum_, [])
                        sum_pairs[sum_].append((i, j)

        # Let top[i] be the sum of largest i numbers. Go to 
        # https://siyuangong.com/projects/#leetcode for other
        # solutions, analysis and updates. 
        top = [0]       
        for i in range(1, N):
            top.append(top[i - 1] + nums[-i])     

        # Find range of the least number in curr_n (0,...,N)
        # numbers that sum up to curr_target, then find range of
        # 2nd least number and so on by recursion. Go to
        # https://siyuangong.com/projects/#leetcode for other
        # solutions, analysis and updates. 
        def sum_(curr_target, curr_n, lo=0):
            if curr_n == 0:
                if curr_target == 0:
                    quadruplets.append(quadruplet[:])
                return
            
            next_n = curr_n - 1
            max_i = len(nums) - curr_n
            max_i = bisect_left(
                nums, curr_target // curr_n,
                lo, max_i)
            min_i = bisect_left(
                nums, curr_target - top[next_n],
                lo, max_i)

            for i in range(min_i, max_i + 1): 
                if i == min_i or nums[i] != nums[i - 1]:
                    quadruplet.append(nums[i])
                    next_target = curr_target - nums[i]
                    sum_(next_target, next_n, i + 1)
                    quadruplet.pop()

        sum_(target, N)
        return quadruplets