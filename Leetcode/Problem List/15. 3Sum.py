class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start,end = i + 1,len(nums) - 1
            while start < end:
                twosum = nums[start] + nums[end]

                if twosum < -nums[i]:
                    start += 1
                elif twosum > -nums[i]:
                    end -= 1
                else:
                    ans.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
        return ans