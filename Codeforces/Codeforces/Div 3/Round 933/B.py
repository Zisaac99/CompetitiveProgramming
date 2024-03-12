t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().rstrip().split()))

    first = 0
    second = 0 
    third = 0
    ans = 'YES'

    for i in range(0,len(a) - 2):
        if first > a[i]:
            ans = 'NO'
            break

        s = a[i] - first

        if i == len(a) - 3:
            first = first + s 
            second = second + (2 * s)
            third = third + s
            if second != a[i+1] or third != a[i+2]:
                ans = 'NO'
        else:
            first = second + (2 * s)
            second = third + s
            third = 0


    print(ans)
    

        