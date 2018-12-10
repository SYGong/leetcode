class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_left, max_len = 0, 0

        def expand_to(ex_l, ex_r):
            # left/right pointer
            if (ex_l >= 0 
                    and ex_r < len(s)                    
                    and s[ex_l] == s[ex_r]):
                expand_to(ex_l - 1, ex_r + 1)
            else:
                pal_len = ex_r - ex_l - 1
                nonlocal max_left, max_len
                if max_len < pal_len:
                    max_left = ex_l + 1
                    max_len = pal_len

        for i in range(len(s)):
            expand_to(i, i)
            expand_to(i, i + 1)
        return s[max_left : max_left + max_len]