class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def conquer(str1,str2):
            ans = ''
            for i in range(min(len(str1),len(str2))):
                if str1[i] != str2[i]:
                    break
                ans += str1[i]
            return ans

        def DivideandConquer(list):
            if len(list) < 2:
                return list[0]
            
            n = len(list) // 2

            return conquer(DivideandConquer(list[n:]),DivideandConquer(list[:n]))

        return DivideandConquer(strs)