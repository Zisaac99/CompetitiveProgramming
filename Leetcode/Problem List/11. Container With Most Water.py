class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0
        ans = -1

        for _ in range(end):
            area = min(height[start],height[end]) * (end-start)
            if area > ans:
                ans = area

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return ans
