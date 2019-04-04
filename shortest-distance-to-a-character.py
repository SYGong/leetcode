class Solution:
    def shortestToChar(self, S: 'str', C: 'str') -> 'List[int]':
        n = len(S)
        res = [0] * n
        prev_e = -1
        for i in range(n):
            if S[i] == C:
                res[i] = 0
                if prev_e < 0:
                    for j in range(i):
                        res[j] = i-j
                else:
                    mid = (prev_e + i + 1)//2
                    for j in range(prev_e+1, mid):
                        res[j] = j - prev_e
                    for j in range(mid, i):
                        res[j] = i-j
                prev_e = i
        for j in range(prev_e+1, n):
            res[j] = j - prev_e
        return res