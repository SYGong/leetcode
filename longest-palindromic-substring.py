class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        if s == s[::-1]:
            return s
        
        start = 0
        max_length = 1
        
        for i in range(2, len(s) + 1):
            if i - max_length - 2 >= 0:
                temp = s[i - max_length - 2: i]
                if temp == temp[::-1]:
                    start = i - max_length - 2
                    max_length += 2
                    continue
            
            if i - max_length - 1 >= 0:
                temp = s[i - max_length - 1: i]
                if temp == temp[::-1]:
                    start = i - max_length - 1
                    max_length += 1
                    
        return s[start: start + max_length]