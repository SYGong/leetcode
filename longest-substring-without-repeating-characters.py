class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_start = 0
        char_index = {}
        max_len = 0
        for i, c in enumerate(s):
            if c in char_index and char_index[c] >= sub_start:
                sub_start = char_index[c] + 1
                if len(s) - sub_start < max_len:
                    break
            else:
                max_len = max(i - sub_start + 1, max_len)
            char_index[c] = i            
        return max_len