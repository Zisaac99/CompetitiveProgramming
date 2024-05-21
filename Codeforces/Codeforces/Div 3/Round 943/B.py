t = int(input())
for _ in range(t):
    nm = list(map(int,input().rstrip().split()))
    n, m = nm[0], nm[1]
    a = input()
    b = input()

    c,d = 0, 0

    while c < n and d < m:
        if a[c] == b[d]:
            c += 1
        d += 1

    print(c)
