t = int(input())

for case in range(t):
    s,h = list(map(int,input().rstrip().split()))
   

    r_score = 0
    y_score = 0

    dict = {}

    r_inside = 0
    y_inside = 0

    n = int(input())

    for _ in range(n):
        x, y = list(map(int,input().rstrip().split()))
        dist = ((y - 0)**2 + (x-0)**2)**0.5 - s
        dict[dist] = 'r'
        if dist <= h:
            r_inside += 1

    m = int(input())

    for _ in range(m):
        z,w = list(map(int,input().rstrip().split()))
        dist = ((z - 0)**2 + (w-0)**2)**0.5 - s
        if dist in dict:
            dict[dist] += 'y'
        else:
            dict[dist] = 'y'
        if dist <= h:
            y_inside += 1

    if r_inside > 0 and y_inside > 0:
        val = list(dict.keys())
        val = sorted(val)
        key = []
        for i in val:
            key.append(dict[i])

        r = key.index('r')
        y = key.index('y')

        try:
            ry = key.index('ry')
        except:
            if r != 0:
                print(f'Case #{case + 1}: {0} {r}')
            else:
                print(f'Case #{case + 1}: {y} {0}')
    else:
        print(f'Case #{case + 1}: {r_inside} {y_inside}')
   

    