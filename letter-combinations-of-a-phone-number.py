class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m ={'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        if len(digits) == 0:
            return []
        
        res = [""]
        
        for d in digits:
            res = [i+j for i in res for j in m[d]]
            
        return res