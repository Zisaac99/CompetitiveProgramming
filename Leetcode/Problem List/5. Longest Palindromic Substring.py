class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        
        def expand_ard_center(s,idx1,idx2):
            if (idx1 >= 0 and idx2 < len(s)) and s[idx1] == s[idx2] :
                while (idx1 >= 0 and idx2 < len(s)) and (s[idx1] == s[idx2]):
                    idx1 -= 1
                    idx2 += 1
                return idx1+1,idx2
            else:
                return idx1,idx2-1

        for i in range(len(s)):
            i1,i12 = expand_ard_center(s,i,i)
            i2,i22 = expand_ard_center(s,i,i+1)

            idx1,idx2 = [i1,i12] if i12 - i1 > i22 - i2 else [i2,i22]
            cans = s[idx1:idx2]
            if len(cans) > len(ans):
                ans = cans
        return ans