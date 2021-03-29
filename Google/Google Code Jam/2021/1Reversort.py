t = int(input())
for c in range(t):
    n = int(input()) 
    l = list(map(int,input().rstrip().split()))
    ll = len(l)
    cost = 0
    for i in range(ll - 1):
        j = l.index(min(l[i:ll]))
        cost += j - i + 1
        l[i:j+1] = reversed(l[i:j+1])
    print(f'Case #{c + 1}: {cost}')