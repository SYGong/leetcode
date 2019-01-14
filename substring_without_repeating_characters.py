class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        "dvdf  3"
        
       
        dic=[-1]*256 
        maxLen = 0
        start = -1;
        for i,e in enumerate(s):
            if (dic[ord(e)] > start):
                start = dic[ord(e)]
            dic[ord(e)] = i;
            maxLen = max(maxLen, i - start);
        
        return maxLen;