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

strs = ['flow']


def conquer(str1,str2):
    ans = ''
    for i in range(min(len(str1),len(str2))):
        if str1[i] != str2[i]:
            break
        ans += str1[i]
    return ans

def DivideandConquer(list):
    if len(list) < 2:
        return list[0]
    
    n = len(list) // 2

    return conquer(DivideandConquer(list[n:]),DivideandConquer(list[:n]))

print(DivideandConquer(strs))