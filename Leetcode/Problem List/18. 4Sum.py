class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(arr, target,k):
            ans = []

            if not arr or len(arr) < 2:
                return ans
            
            if arr[0] > (target / k):
                return ans
            
            if arr[-1] < (target / k):
                return ans
            
            if k == 2:
                return twoSum(arr,target)
            
            for i in range(len(arr)):
                if i == 0 or arr[i] != arr[i-1]:
                    for subset in kSum(arr[i+1:],target - arr[i],k - 1):
                        ans.append([arr[i]] + subset)
            
            return ans

        def twoSum(arr,target):
            start = 0
            end = len(arr) - 1
            store = []
            while start < end:
                sum = arr[start] + arr[end]

                if sum < target or (start > 0 and arr[start] == arr[start - 1]):
                    start += 1
                elif sum > target or (end < len(arr) - 1 and arr[end] == arr[end + 1]):
                    end -= 1
                elif sum == target:
                    store.append([arr[start],arr[end]])
                    start += 1
                    end -= 1
            return store

        nums.sort()
        return kSum(nums,target,4)
