t = int(input())
for _ in range(t):
    n = int(input())

    ans = ''
    if n % 2 == 1:
        print('NO')
    else:
        print('YES')

        for i in range(1,int(n/2)+1):
            if i % 2 == 0:
                ans += 'AA'
            else:
                ans += 'BB'

        print(ans)
