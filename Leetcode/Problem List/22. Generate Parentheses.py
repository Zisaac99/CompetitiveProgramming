class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(str,open,close):
            if open == n and close == n:
                ans.append(str)
                return 
            
            if open < n:
                dfs(str + '(',open + 1,close)

            if close < open:
                dfs(str + ')',open,close + 1)


        dfs('',0,0)
        return ans