class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        rev_x = 0
        while x > rev_x:
            rev_x *= 10 
            rev_x += x % 10
            x //= 10
        return x == rev_x or x == rev_x // 10