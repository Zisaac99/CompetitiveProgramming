# Iterative Solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ht ={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        ans = []
        for i in digits:
            if len(ans) == 0:
                ans = ans + ht[i]
            else:
                arr = []
                for j in ans:
                    for k in ht[i]:
                        arr.append(j + k)
                ans = arr
        return ans
    

# Recursive Solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ht ={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        ans = []
        def backtrack(combination,digitsIndex):
            if digitsIndex == len(digits):
                ans.append(combination)
                return 
            
            for i in ht[digits[digitsIndex]]:
                backtrack(combination + i,digitsIndex + 1)

        backtrack('',0)
        return ans