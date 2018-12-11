class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        pairs = []
        for i, v in enumerate(words):
            for j, w in enumerate(words):
                if (i != j 
                    and v + w == w[::-1] + v[::-1]):
                    pairs.append([i, j])
        return pairs