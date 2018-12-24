from collections import Counter

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        TARGET = 0
        num_freq = Counter(nums)
        nums = sorted(num_freq)
        # unique numbers in ascending order

        triplets = []
        for i, v in enumerate(nums):
            if num_freq[v] >= 2:
                if v * 3 == TARGET and num_freq[v] >= 3:
                    triplets.append([v] * 3)
                else:
                    complement = TARGET - 2 * v
                    if complement in num_freq and complement != v:
                        triplets.append([v] * 2 + [complement])
            if v * 3 < TARGET:
                two_sum = TARGET - v
                for u in nums[i + 1 : -1]:
                    if 2 * u >= two_sum:
                        break
                    complement = two_sum - u
                    if complement in num_freq:
                        triplets.append([v, u, complement])
        return triplets