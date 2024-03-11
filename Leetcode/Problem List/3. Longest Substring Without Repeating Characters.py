class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        ans = 0
        start = 0

        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= start:
                if len(s[start:i]) > ans: 
                    ans = len(s[start:i])
                start = dict[s[i]] + 1
            elif i == len(s) - 1:
                if len(s[start:i+1]) > ans: 
                    ans = len(s[start:i+1])
            dict[s[i]] = i

        return ans