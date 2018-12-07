class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub_first, sub_last, max_len = 0, 0, 0
        for core in range(len(s)):
            for arm in range(min(core, len(s) - 1 - core)):
                if s[core + arm] == s[core - arm]:
                    if 1 + arm * 2 > sub_last - sub_first:
                        sub_first = core - arm
                        sub_last = core + arm
                        max_len = sub_last - sub_first + 1
                else:                    
                    break
        
        for core in range(len(s) - 1):
            for arm in range(1, min(core + 1, len(s) - 1 - core)):
                if s[core - arm + 1] == s[core + arm]:
                    if arm * 2 > max_len:
                        sub_first = core - arm + 1
                        sub_last = core + arm
                        max_len = sub_last - sub_first + 1
                else:                    
                    break
        return s[sub_first : sub_last + 1]