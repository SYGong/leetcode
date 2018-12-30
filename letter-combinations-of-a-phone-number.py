class Solution:
    DIGITS_MAP = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return [letter for letter in self.DIGITS_MAP[digits[0]]]

        combos = []
        for option in self.letterCombinations(digits[1:]):
            for letter in self.DIGITS_MAP[digits[0]]:
                combos.append(letter+option)
        return combos