class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict:
                return [i,dict[diff]]
            dict[nums[i]] = i