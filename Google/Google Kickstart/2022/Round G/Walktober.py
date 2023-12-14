t = int(input())

for case in range(t):
    m, n , p = list(map(int,input().rstrip().split())) # denoting the total number of participants, the total number of days the competition runs, 
                                                       #and the last year participant ID of John

    scoreboard = [[] for i in range(n)]
    for _ in range(m):
        inp = list(map(int,input().rstrip().split()))
        for i in range(n):
            scoreboard[i].append(inp[i])

    ans = 0
    j_score = 0
    sorted_score = []
    for i in range(n):
        j_score = scoreboard[i][p-1]
        sorted_score = sorted(scoreboard[i],reverse = True)
        ans += sorted_score[0] - j_score
        
    print(f'Case #{case+1}: {ans}')
            

