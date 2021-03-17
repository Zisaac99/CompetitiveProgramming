n = int(input())
na = list(map(int,input().rstrip().split()))
s = (n * (n + 1)) / 2
print(int(s - sum(na)))