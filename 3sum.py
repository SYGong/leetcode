from bisect import bisect, bisect_left

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        if len(nums) < N:
            return triplets
        nums = sorted(nums)
        triplet = []

        # Let top[i] be the sum of largest i numbers. Go to 
        # https://siyuangong.com/projects/#leetcode for other
        # solutions, analysis and updates. 
        top = [
            0,
            nums[-1],
            nums[-1] + nums[-2]           
        ]

        # Find range of the least number in curr_n (0,...,N)
        # numbers that sum up to curr_target, then find range of
        # 2nd least number and so on by recursion. Go to 
        # https://siyuangong.com/projects/#leetcode for other
        # solutions, analysis and updates. 
        def sum_(curr_target, curr_n, lo=0):
            if curr_n == 0:
                if curr_target == 0:
                    triplets.append(triplet[:])
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
                    triplet.append(nums[i])
                    next_target = curr_target - nums[i]
                    sum_(next_target, next_n, i + 1)
                    triplet.pop()

        sum_(0, N)
        return triplets