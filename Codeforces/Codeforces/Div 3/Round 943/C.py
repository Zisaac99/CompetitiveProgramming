t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int,input().rstrip().split()))
    ans = [501]
    prev = -1
    for i in range(len(x)):
        if x[i-1] == 0:
            ans.append(x[i])
        else:
            ans.append(x[i] + ans[i])
    print(*ans)