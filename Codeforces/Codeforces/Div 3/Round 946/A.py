import math
t = int(input())
for _ in range(t):
    xy = list(map(int,input().rstrip().split()))
    x, y = xy[0], xy[1]
    yscreens = math.ceil(y/2) # find number of screens needed for y as one screen can only fit max 2 y
    screensleft =  (yscreens * 15) - (4* y) # based on the total number of screens needed for y we compute how many space is left
    if screensleft - x >= 0:
        print(yscreens)
    else:
        ans =  yscreens + math.ceil((x - screensleft)/15)
        print(ans)
