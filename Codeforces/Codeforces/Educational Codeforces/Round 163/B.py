t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int,input().rstrip().split()))

    sorted = 'YES'
    i = -1

    while i < len(a) - 1:
        i += 1
        if i == len(a) - 1:
            if a[i] < a[i-1]:
                sorted = 'NO'
                break
        elif a[i] > a[i+1]:
            if len(str(a[i])) == 1:
                sorted = 'NO'
                break
            else:
                a.insert(i+1,int(str(a[i])[0]))
                a.insert(i+2,int(str(a[i])[1]))
                a.pop(i)
                if i == 0:
                    i -= 1
                else:
                    i -= 2

    print(sorted)

