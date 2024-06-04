from math import *
t = int(input())
for _ in range(t):
    nm = list(map(int,input().rstrip().split()))
    n,m = nm[0],nm[1]
    arr = list(map(int,input().rstrip().split()))
    arr = [i%m for i in arr]
    arrCount = [0] * m
    ans = 0

    for i in arr:
        arrCount[i] += 1

    if arrCount[0]:
        ans += 1

    for i in range(1,len(arrCount)):
        diff = m - i
        rem = abs(arrCount[i] - arrCount[diff])

        if not arrCount[i]:
            continue

        if not arrCount[diff]:
            ans += arrCount[i]
            arrCount[i] = 0
        else:
            if rem <= 1:
                ans += 1
            else:
                ans += rem
            arrCount[i] = 0
            arrCount[diff] = 0

    print(ans)




    




        



