t = int(input())

for i in range(t):
    n,b = list(map(int,input().rstrip().split()))
    a = list(map(int,input().rstrip().split()))
    currenta = sorted(a,reverse = True)
    asum = sum(currenta)
    nhouses = n
    if asum <= b:
        print(f'Case #{i+1}: {n}')
    elif min(currenta) > b:
        print(f'Case #{i+1}: 0')
    else:
        currentaleft = asum
        for j in currenta:
            currentaleft -= j
            nhouses -= 1
            if currentaleft <= b:
                break
        print(f'Case #{i + 1}: {nhouses}')