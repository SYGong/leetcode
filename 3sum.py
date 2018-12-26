class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        pos = [p for p in freq if p > 0]
        neg = [n for n in freq if n < 0]
        
        if 0 in freq and freq[0] > 2:
            ans = [[0,0,0]]
        else: 
            ans = []
        
        for p in pos:
            for n in neg:
                s = - (p+n)
                if s in freq:
                    if s == p and freq[p] > 1:
                        ans.append([n,s,p])
                    if s == n and freq[n] > 1:
                        ans.append([n,s,p])
                    elif s < p and s > n:
                        ans.append([n,s,p])
                        
                        
        return ans