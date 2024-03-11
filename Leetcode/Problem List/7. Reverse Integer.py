class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)

        if s[0] == '-':
            ans = int('-' + s[1:][::-1])
        else:
            ans = int(s[::-1])
            
        if ans < (-2 ** 31) or ans > ((2 ** 31) - 1):
            return 0
        return ans