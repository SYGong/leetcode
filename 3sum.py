class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                two_sum = -nums[i]
                incre = i + 1
                decre = len(nums) - 1 
                while incre < decre and 2 * nums[incre] <= two_sum and 2 * nums[decre] >= two_sum:
                    if nums[incre] + nums[decre] == two_sum:
                        triplets.append([nums[i], nums[incre], nums[decre]])
                        if nums[incre] == nums[decre]:
                            break
                        incre += 1
                        decre -= 1
                        while incre < decre and nums[incre - 1] == nums[incre]:
                            incre += 1
                        while incre < decre and nums[decre + 1] == nums[decre]:
                            decre -= 1
                    elif nums[incre] + nums[decre] > two_sum:
                        decre -= 1
                    else:
                        incre += 1
        return triplets