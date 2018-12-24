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
                    triplets.appned([v] * 3)
                    break
                else:
                    complement = TARGET - 2 * v
                    if complement in num_freq:
                        triplets.append([v] * 2 + [complement])
            elif v < 0:
                two_sum = TARGET - v
                incre = i + 1
                decre = len(nums) - 1 
                while incre < decre and 2 * nums[incre] <= two_sum and 2 * nums[decre] >= two_sum:
                    if nums[incre] + nums[decre] == two_sum:
                        triplets.append([v, nums[incre], nums[decre]])
                        incre += 1
                        decre -= 1
                    elif nums[incre] + nums[decre] > two_sum:
                        decre -= 1
                    else:
                        incre += 1
        return triplets