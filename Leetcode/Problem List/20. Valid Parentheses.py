class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        dict = {'(':')', '{':'}','[':']'}
        for c in s:
            if c in dict:
                queue.append(c)
            else:
                if len(queue) == 0 or dict[queue.pop()] != c:
                    return False

        return len(queue) == 0