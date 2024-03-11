t = int(input())
for _ in range(t):
    arr_l = int(input())
    arr = list(map(int,input().rstrip().split()))

    arr = sorted(arr)

    i,k,l,j = arr[0],arr[1],arr[-2],arr[-1]
    ans = abs(i-j) + abs(j-k) + abs(k-l) + abs(l-i)
    print(ans)
