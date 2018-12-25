class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # j=999
        # for each in strs:
        #     a = len(each)
        #     if a<j:
        #         j=a
        # b=0
        # while b < len(strs):
        #     a=strs[0][0:j]
        #     if a in strs[b][0:j]:
        #         b+=1
        #     else:
        #         b+=1
        #         j=j-1
        #     if j==0:
        #         return ''
        # return a
                
        # a=0
        # while a<=j:
        #     for x in range(len(strs)):
        #         result.append(strs[x][a])
        #         if strs[a][x] in result:
        #             continue
        #         else:
        #             result.pop()
        #             return result
        #     a+=1
        # return result
        commonPrefix = strs[0]
        for string in strs:
            commonPrefix = self.findPrefix(commonPrefix,string)

        return commonPrefix

    def findPrefix(self,prefix, string):
        while prefix is not "":
            
            if string.startswith(prefix):
                
                return prefix
            else:
                prefix = prefix[:-1]

        return ""