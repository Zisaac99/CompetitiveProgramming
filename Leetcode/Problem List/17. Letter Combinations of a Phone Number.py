# Iterative Solution
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