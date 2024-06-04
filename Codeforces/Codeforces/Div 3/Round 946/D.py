t = int(input())

def solve():
    n = int(input())
    s = input()

    dir = {
        'N': [0,1],
        'S': [0,-1],
        'E': [1,0],
        'W': [-1,0]
    }
    x,y = 0,0
    ans = ''

    for d in s:
        x,y = x + dir[d][0], y + dir[d][1]

    if x % 2 == 1 or y % 2 == 1:
        return 'NO'
    
    if s == 'NS' or s == 'SN' or s == 'EW' or s == 'WE':
        return 'NO'
        
    targetX, targetY = int(x/2), int(y/2)
    currX, currY = 0,0
    targetDist = abs(targetX - currX) + abs(targetY - currY)
    count = 0

    for d in s:
        newX, newY = currX + dir[d][0], currY + dir[d][1]
        newtargetDist = abs(targetX - newX) + abs(targetY - newY)

        if count == 0 or (newtargetDist < targetDist):
            count += 1
            ans += 'R'
            currX,currY = newX, newY
            targetDist = newtargetDist
        else:
            ans += 'H'

    return ans

for _ in range(t):
    print(solve())



