t = int(input())
for _ in range(t):
    # n = int(input())
    # a = list(map(int,input().rstrip().split()))
    # ua = sorted(list(set(a)))
    # uac = []
    # da = []
    # dac = []
    # for i in ua:
    #     uac.append(a.count(i))
    # for i in range(len(uac)):
    #     if uac[i] > 1:
    #         da.append(ua[i])
    #         dac.append(uac[i] - 1)
    
    # for i in range(len(da)):
    #     for j in range(dac[i]):
    #         ua.append(da[i])
    
    # ans = ''
    # for i in range(len(ua)):
    #     if i != len(ua) - 1:
    #        ans += str(ua[i]) + ' '
    #     else:
    #         ans += str(ua[i])
    # print(ans)

    n = int(input())
    arr1 = list(map(int,input().rstrip().split()))
    arr1.sort()
    s = set()
    arr2 = []
    for i in arr1:
        if i in s:
            arr2.append(i)
        else:
            s.add(i)
    ans = sorted(list(s)) + arr2
    print(*ans)


