class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 999999
        nums.sort()

        for i in range(len(nums)):
            start,end = i + 1,len(nums) - 1
            while start < end:
                currentAns = nums[i] + nums[start] + nums[end]
                diff = abs(target - currentAns) 

                if diff < abs(target-ans):
                    ans = currentAns

                if currentAns == target:
                    return ans
                elif currentAns < target:
                    start += 1
                else:
                    end -= 1
        return ans