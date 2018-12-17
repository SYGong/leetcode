import math

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
        digits = int(math.log10(x)) + 1
        rev_x = 0
        for d in range(digits // 2):
            rev_x *= 10 
            rev_x += x % 10
            x //= 10
        if digits % 2 == 1:
            x //= 10
        return x == rev_x