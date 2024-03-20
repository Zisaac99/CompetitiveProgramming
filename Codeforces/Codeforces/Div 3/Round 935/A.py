t = int(input())
import math
for _ in range(t):
    abc = list(map(int,input().rstrip().split()))
    a, b, c = abc[0], abc[1], abc[2]
    bneeded = 0 if b % 3 == 0 else 3 - (b%3)
    cleft = c - bneeded
    if bneeded == 0:
        print(int(a + (b/3) + math.ceil(c/3)))
    else:
        if cleft < 0:
            print(-1)
        else:
            print(int(a + ((b//3) + 1) + math.ceil(cleft/3)))
