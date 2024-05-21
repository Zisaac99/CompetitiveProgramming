t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().rstrip().split()))
    ans = 0
    dict  = {}
    dict1 = {}
    dict2 = {}
    dict3 = {}

    for i in range(n - 2):
        a,b,c = arr[i],arr[i+1],arr[i+2]

        if (a,b,c) in dict:
            dict[(a,b,c)] += 1
        else:
            dict[(a,b,c)] = 1

        if (a,b) in dict1:
            dict1[(a,b)] += 1
        else:
            dict1[(a,b)] = 1

        if (a,c) in dict2:
            dict2[(a,c)] += 1
        else:
            dict2[(a,c)] = 1

        if (b,c) in dict3:
            dict3[(b,c)] += 1
        else:
            dict3[(b,c)] = 1

        ans += dict1[(a,b)] + dict2[(a,c)] + dict3[(b,c)] - (dict[(a,b,c)] * 3)

    print(ans)

    

    
    