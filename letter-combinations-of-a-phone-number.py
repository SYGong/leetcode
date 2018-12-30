class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_char = [
            '',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]
        
        combinations = []

        def dfs(letters, digits):
            nonlocal combinations
            if digits == '':
                if letters != '': 
                    combinations.append(letters)
                return
            for c in num_char[int(digits[0])]:
                dfs(letters + c, digits[1:])
                
        dfs('', digits)
        return combinations