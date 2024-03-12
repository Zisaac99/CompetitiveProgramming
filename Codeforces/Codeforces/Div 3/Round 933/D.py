t = int(input())
for _ in range(t):
    nmk = list(map(int,input().rstrip().split()))
    n, m, x = nmk[0], nmk[1], nmk[2] # n number of players. m number of throws, x who had the ball first

    arr = []
    for i in range(m):
        arr.append(list(map(str,input().rstrip().split())))
        arr[i][0] = int(arr[i][0])

    holders = set()
    holders.add(x)
    for i in range(len(arr)):
        currHolders = set()
        for j in holders:
            pos = j + arr[i][0]
            if pos > n:
                pos = pos - n

            neg = j - arr[i][0]
            if neg <= 0:
                neg = neg + n 

            if arr[i][1] == '0':
                currHolders.add(pos)
            elif arr[i][1] == '1':
                currHolders.add(neg)
            else:
                currHolders.add(pos)
                currHolders.add(neg)
        holders = currHolders

    players = sorted(holders)

    playersLen = len(holders)
    ans = ''
    for i in range(playersLen):
        if i == playersLen - 1:
            ans += str(players[i])
        else:
            ans += str(players[i]) + ' '

    print(playersLen)
    print(ans)
    

        




