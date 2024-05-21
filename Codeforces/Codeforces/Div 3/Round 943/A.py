import math
t = int(input())
for _ in range(t):
    x = int(input())
    max = -1
    ans = -1
    for i in range(1,x):
        curr = math.gcd(x,i) + i
        if curr > max:
            max = curr
            ans = i
        
    print(ans)
