t = int(input())
for _ in range(t):
    nmk = list(map(int,input().rstrip().split()))
    a, b, m = nmk[0], nmk[1], nmk[2]
    print((m//a) + (m//b) + 2)