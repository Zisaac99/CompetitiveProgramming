n = int(input())
a = list(map(int,input().rstrip().split()))
moves = 0
for i in range(1,n):
    if a[i] < a[i-1]:
        moves += a[i-1] - a[i]
        a[i] = a[i-1]
print(moves)
        
 