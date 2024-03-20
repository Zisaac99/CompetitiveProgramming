t = int(input())
for _ in range(t):
    nmk = list(map(int,input().rstrip().split()))
    n, m, k = nmk[0], nmk[1], nmk[2]
    left = sorted(list(map(int,input().rstrip().split())))
    right = sorted(list(map(int,input().rstrip().split())))