class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        pairs = []
        for i, v in enumerate(words):
            for j, w in enumerate(words):
                if i != j and self.isPair(v, w):
                    pairs.append([i, j])
        return pairs
    
    def isPair(self, a, b):
        if len(a) <= len(b):
            for i in range(len(a)):
                if a[i] != b[-i - 1]:
                    return False
            b = b[:len(b) - len(a)]
            for i in range(len(b) // 2):
                if b[i] != b[-i -1]:
                    return False
            return True
        else:
            for i in range(len(b)):
                if a[i] != b[-i - 1]:
                    return False
            a = a[len(b):]
            for i in range(len(a) // 2):
                if a[i] != a[-i -1]:
                    return False
            return True