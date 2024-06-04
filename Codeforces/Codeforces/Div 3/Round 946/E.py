t = int(input())
for _ in range(t):
    mx = list(map(int,input().rstrip().split()))
    m, x = mx[0], mx[1]

    bal = 0

    costArr = []
    happArr = []

    for _ in range(m):
        ch = list(map(int,input().rstrip().split()))
        c,h = ch[0],ch[1]
        costArr.append(c)
        happArr.append(h)
    
    maxH = sum(happArr)
    dp = [0] + [float('inf')] * maxH

    for i in range(m):
        for j in range(maxH,happArr[i] - 1,-1):
            if dp[j-happArr[i]] + costArr[i] <= bal:
                dp[j] = min(dp[j],dp[j-happArr[i]] + costArr[i])
        bal += x

    for i in range(len(dp) - 1,-1,-1):
        if dp[i] != float('inf'):
            print(i)
            break


    # def knapsack(b, th, c , h, ph, i): # balance, total happiness, cost array, happiness array, iterator
    #     if i > 0:
    #         ht2[(i-1,ph)] = b
            
    #     if i == m:
    #         return th
        
    #     if (i,th) in ht and ht2[(i,th)] >= b:
    #         return ht[(i,th)]
        
    #     if b - c[i] < 0:
    #         ht[(i,th)] = knapsack(b, th, c, h, th, i+1)
    #     else:
    #         ht[(i,th)] = max(knapsack(b - c[i] + x, th + h[i], c, h, th, i+1), knapsack(b + x, th, c, h, th, i+1))
    #     return ht[(i,th)]
        
    #print(f'Ans: {knapsack(0,0,costArr,happArr,0)}')
    #print(knapsack(0,0,costArr,happArr,0,0))


    




    

