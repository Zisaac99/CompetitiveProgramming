t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())

    ans = 0
    deduct = 0
    l = len(s)
    for i in range(l):
        if i + 3 < l + 1 and (s[i:i+3] == 'pie' or s[i:i+3] == 'map'):
            ans += 1
        if i + 5 < l + 1 and (s[i:i+5] == 'mapie'):
            deduct += 1
    print(ans - deduct)