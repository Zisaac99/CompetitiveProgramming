t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().rstrip().split()))
    ans = 0
    ht  = {}

    for i in range(n - 2):
        a,b,c = arr[i],arr[i+1],arr[i+2]
        bt = [0] * 3
        trip = (a,b,c)

        bt[0] = (a,b,0)
        bt[1] = (a,0,c)
        bt[2] = (0,b,c)

        for t in bt:
            ans += ht.get(t,0) - ht.get(trip,0)
            ht[t] = ht.get(t,0) + 1
        ht[trip] = ht.get(trip,0) + 1
        

    print(ans)

    

    
    