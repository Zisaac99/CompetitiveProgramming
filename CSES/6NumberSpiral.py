t = int(input())
yx = [[int(j) for j in input().rstrip().split()] for i in range(t)]
for i in range(t):
    y,x = yx[i][0],yx[i][1]
    larger = 0
    if y > x:
        larger = y
    else:
        larger = x

    yl,xl = 0,0
    yd,xd = 0,0
    if larger % 2== 0:
        yl,xl = larger,1
    else:
        yl,xl = 1,larger
    yd,xd = abs(yl-y),abs(xl-x)

    largestval = larger ** 2
    print(largestval - (yd + xd))