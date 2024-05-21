t = int(input())
for _ in range(t):
    a = int(input())
    b = input()
    s = set()

    for char in b:
        s.add(char)

    c = sorted(list(s))
    clen = len(c)
    ans = ''
    for i in b:
        ind = c.index(i)
        ans += c[clen - (ind+1)]

    print(ans)

