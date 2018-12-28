from bisect import bisect, bisect_left


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        cumu_max = [0, nums[-1], nums[-1] + nums[-2]]
        min_diff = float('inf')
        three_sum = None

        # Denotes the least one of num_ints (1,2,3...)
        # integers by x, this function return
        # smallest/largest index of x.
        def lst(sum_, num_ints, lo=0):
            nonlocal cumu_max, nums
            num_ints_remain = num_ints - 1
            most_i = bisect(
                nums, sum_ // num_ints,
                lo, len(nums) - num_ints)
            least_v = sum_ - cumu_max[num_ints_remain]
            least_i = bisect_left(
                nums, least_v, 
                lo, len(nums) - num_ints) - 1

            least_i = max(least_i, lo)
            return least_i, most_i+1

        # Consider smallest number in triplets
        a0, a1 = lst(target, 3)
        for i in range(a0, a1):
            two_sum = target - nums[i]
            b0, b1 = lst(two_sum, 2, i + 1)
            for j in range(b0, b1):
                complement = two_sum - nums[j]
                c0, c1 = lst(complement, 1, j + 1)
                for w in nums[c0:c1]:
                    diff = abs(complement - w)
                    if diff == 0:
                        return nums[i] + nums[j] + w
                    elif diff < min_diff:
                        min_diff = diff
                        three_sum = nums[i] + nums[j] + w
        return three_sum


def main():
    solu = Solution()
    a = [-1, 2, 1, -4]
    #b = [0, 1, 2]
    c = [0,0,0]
    print(solu.threeSumClosest(c, 1))
    #print(solu.threeSumClosest(b, 0))
    print(solu.threeSumClosest(a, 1))

if __name__ == "__main__":
    main()
