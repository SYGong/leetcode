class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        testing = str(x)
        return testing[::-1] == str(x)