t = int(input())
nc = [list(map(int,input().rstrip().split())) for i in range(t)]
for a in range(t):
    n = nc[a][0]
    c = nc[a][1]
    if (n - 1) <= c <= (((n * (n + 1))/2) - 1):
        cpl = [1 for i in range(n - 1)]
        cc = c - (n - 1)
        for i in range(len(cpl)):
            aval = n - (i + 1)
            if cc - aval <= 0:
                cpl[i] = cpl[i] + cc
                break
            else:
                cpl[i] = cpl[i] + aval
                cc -= aval
        simulationlist = [i for i in range(n)]
        simulationlistcopy = simulationlist.copy()
        nlist = [i for i in range(1,n + 1)]
        for i in range(n - 1):
            j = cpl[i] + i - 1
            simulationlistcopy[i:j+1] = reversed(simulationlistcopy[i:j+1])
        solutionliststr = ''
        for i in range(len(simulationlist)):
            if i <= len(simulationlist) - 1:
                solutionliststr += str(nlist[simulationlistcopy.index(simulationlist[i])]) + ' '
            else: 
                 solutionliststr += str(nlist[simulationlistcopy.index(simulationlist[i])])
        print(f'Case #{a + 1}: {solutionliststr}')
    else:
        print(f'Case #{a + 1}: IMPOSSIBLE')
