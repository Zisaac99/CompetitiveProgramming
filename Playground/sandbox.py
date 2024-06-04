x = 500
dp = [0,1] + [0] * (x-1)


for i in range(2,x+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[x])