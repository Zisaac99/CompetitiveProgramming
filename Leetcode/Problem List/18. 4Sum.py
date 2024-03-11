class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            for i in range(j+1,len(nums)):
                if i > j+1 and nums[i] == nums[i-1]:
                    continue
                start,end = i + 1,len(nums) - 1
                while start < end:
                    foursum = nums[j] + nums[i] + nums[start] + nums[end]

                    if foursum < target:
                        start += 1
                    elif foursum > target:
                        end -= 1
                    else:
                        print(j,i,start,end)
                        ans.append([nums[j],nums[i],nums[start],nums[end]])
                        start += 1
                        end -= 1

                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
        return ans