# def fib(x):
#     if x <= 1:
#         return 1
#     elif dp[x] != -1:
#         return dp[x]
        
#     dp[x] = fib(x-1) + fib(x-2)

#     return dp[x]

# def fib(x):
#     dp = [-1] * (x+2)
#     dp[0] = 1
#     dp[1] = 1
#     for i in range(2,x+1):
#         dp[i] = dp[i-1] + dp[i-2]

#     return dp[x]

# x = 10
# dp = [-1] * (x+1)

# for i in range(x):
#     print(fib(i))

# def coinChange(coins, amount):
        
#    dp = {}
    
#    for i in coins:
#       dp[i] = 1
   
#    def getResult(amount):
      
#       if amount == 0:
#          return 0

#       if amount in dp:
#          return dp[amount]

#       ans = float('inf')
#       for i in coins:
#          if i <= amount:
#             ans = min(ans, 1 + getResult(amount - i))
      
#       dp[amount] = ans
#       return dp[amount]
   
#    a = getResult(amount)

#    if a != float('inf'):
#       print(a)
#    else:
#       print(-1)

# coinChange([5],11)       
      

# def coinsHMW(coins,target):
#    memo = {}

   
#    for i in range(1,target + 1):
#       memo[i] = 0


#    memo[0] = 1

#    for i in range(1,target+1):
#       for c in coins:
#          if c <= i:
#             memo[i] += memo[i-c]

#    return memo[target]

# print(coinsHMW([1,4,5,8],87))


# def coinsHMW(coins,target):
   
#    dp  = {}
#    ans = 0
#    def getResult(amount):
#       nonlocal ans
#       if amount == 0:
#          return 1
      
#       if amount in dp:
#          return dp[amount]
      
#       # ans = 0
#       for i in coins:
#          if i > amount:
#             return 0
#          else:
#             t = getResult(amount - i)
#             ans += t

#       dp[amount] = ans
#       return ans
   
#    return getResult(target)

# print(coinsHMW([1,2,5],5))

      

# amount = 5
# coins = [1,2,5]
# dp= {}
# def coinsHMW(amount,index):
#    if amount == 0:
#       return 1
   
#    if amount < 0:
#       return 0
   
#    if index == len(coins):
#       return 0
   
#    if (amount,index) in dp:
#       return dp[(amount,index)] 


#    dp[(amount,index)] = coinsHMW(amount - coins[index], index) + coinsHMW(amount, index + 1)
#    return dp[(amount,index)]

# print(coinsHMW(amount,0))

# nums = [-1,0,1,2,-1,-4] 
# ans = []
# ht = {}

# for i in nums:
#     if i in ht:
#         ht[i] += 1
#     else:
#         ht[i] = 1

# keys = list(ht.keys())

# for i in range(len(keys)):
#     temp_i = ht[keys[i]]
#     ht[keys[i]] -= 1
#     for j in range(i,len(keys)):
#         temp_j = ht[keys[j]]
#         if ht[keys[j]] > 0:
#             ht[keys[j]] -= 1
#             diff = -keys[i] - keys[j]
#             if diff in ht and ht[diff] > 0:
#                 ans.append(sorted([keys[i],keys[j],diff]))
#         ht[keys[j]] = temp_j
#     ht[keys[i]] = temp_i

# ans = [list(x) for x in set(tuple(x) for x in ans)]
# print(ans)


# numbers = [-1,0]
# target = -1

# def twoSum(numbers, target):
#     start = 0
#     end = len(numbers) - 1

#     ans = None

#     while not ans:
#         if numbers[start] + numbers[end] == target:
#             return [start+1,end+1]
#         elif numbers[start] + numbers[end] > target:
#             end -= 1
#         else:
#             start += 1

# print(twoSum(numbers,target))

# nums = [0,0,0,0]
# nums.sort()
# ans = []

# for i in range(len(nums)):
#     if i > 0 and nums[i] == nums[i-1]:
#         continue

#     start,end = i + 1,len(nums) - 1
#     ht = {}
#     while start < end:
#         twosum = nums[start] + nums[end]

#         if twosum < -nums[i]:
#             start += 1
#         elif twosum > -nums[i]:
#             end -= 1
#         else:
#             end -= 1
#             if nums[end] in ht:
#                 continue
#             ans.append([nums[i],nums[start],nums[end]])
#             ht[nums[end]] = 0

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
        if i > 0 and arr[i] == arr[i-1]:
            continue
        print()
        for subset in kSum(arr[i+1:],target - arr[i],k - 1):
            ans.append([arr[i]] + subset)
    
    return ans

def twoSum(arr,target):
    start = 0
    end = len(arr) - 1
    store = []
    while start < end:
        sum = arr[start] + arr[end]
        if sum == target:
            store.append([arr[start],arr[end]])
            start += 1
            end -= 1

            while start < end and arr[end] == arr[end+1]:
                end -= 1

        elif sum < target:
            start += 1
        else:
            end -= 1
    return store

# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['9'],
  '4' : ['8','9'],
  '8' : [],
  '9' : []
}

visited = set() # Set to keep track of visited nodes of graph.
def dfs(visited, graph, node,path,target):  #function for dfs
    path.append(node) 
    if node == target:
        return path
    
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            return dfs(visited, graph, neighbour,path,target)

# target = '9'
# print(dfs(visited, graph, '5',[],target))

# a = [[0,1],[1,0]]

l1 = None
l2 = None

x = l1 or l2
print(x)