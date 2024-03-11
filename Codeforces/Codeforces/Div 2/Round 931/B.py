t = int(input())
for _ in range(t):
    n = int(input())

    dp = [0] + ([float('inf')] * n)
    dp[0] = 0
    
    coins = [1,3,6,10,15]

    for i in range(1,n+1):
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i-j]+1,dp[i])
    print(dp[i])