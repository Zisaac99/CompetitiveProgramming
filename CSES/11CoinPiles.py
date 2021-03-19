t = int(input())
ab = [[int(j) for j in input().rstrip().split()] for i in range(t)]
for i in range(t):
    l = ab[i][0]
    r = ab[i][1]

    if (l == 0 and r == 0)or (l <= r * 2 and r <= l * 2 and (l+r) % 3 == 0):
        # 0 and 0 should also be possible
        # Extreme case where we keep only removing 1 and 2 or 2 and 1 from the left and right pile
        # Since we are only removing 1 and 2 the sum of the number of coins of the piles must be divisble by 3
        print('YES')
    else:
        print('NO')