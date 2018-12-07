class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_left, max_len = 0, 0

        def expand_from(p_left, p_right):
            # p_left(right) is the left(right) end of panlidrome 
            while p_left > 0 and p_right < len(s) - 1 and s[p_left - 1] == s[p_right + 1]:
                p_left -= 1
                p_right += 1
            p_len = p_right - p_left + 1
            nonlocal max_left, max_len
            if max_len < p_len:
                max_left = p_left
                max_len = p_len

        for i in range(len(s)):
            expand_from(i, i)
            if i + 1 < len(s) and s[i] == s[i + 1]:
                expand_from(i, i + 1)

        return s[max_left : max_left + max_len]