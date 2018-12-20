class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    triplet =[nums[i], nums[j], nums[k]]
                    if sum(triplet) == 0:
                        triplets.append(triplet)
            
        return triplets 