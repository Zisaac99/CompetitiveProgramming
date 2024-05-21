class Solution:
    def maxSubArray(self, nums):
        prev = 0
        ans = float('-inf')
        for i in range(len(nums)):
            prev = max(prev + nums[i],nums[i])
            ans = max(prev, ans)

        print(ans)


s = Solution()
s.maxSubArray([-2])

s = [(1,2,3),(8,8,8)]
print(s.index((8,8,8)))



