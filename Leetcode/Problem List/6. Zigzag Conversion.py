class Solution:
    def convert(self, s: str, numRows: int) -> str:
        counter = 0
        increment = True
        arr = ['' for i in range(numRows)]
        ans = ''

        if numRows == 1:
            return s
        for i in s:
            arr[counter] += i
            if increment:
                if counter == numRows - 1:
                    increment = False
                    counter -= 1
                else:
                    counter += 1
            else:
                if counter == 0:
                    increment = True
                    counter += 1
                else:
                    counter -= 1

        for i in arr:
            ans += i

        return ans