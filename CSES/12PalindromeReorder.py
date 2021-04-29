from collections import Counter
s = input()
scount = Counter(s)
if len(scount.keys()) == 1:
    print(s)
else:
    counter = 0
    middle = []
    for i in scount.keys():
        if scount[i] % 2 != 0:
            counter += 1
            middle.append([i,scount[i]])
    sol = ''
    if counter == 1:
        sol = middle[0][1] * middle[0][0]
        scount.pop(middle[0][0])
        for i in scount.keys():
            sol = (int(scount[i]/2) * i) + sol + (int(scount[i]/2) * i)
        print(sol)
    elif counter == 0:
        for i in scount.keys():
            sol = (int(scount[i]/2) * i) + sol + (int(scount[i]/2) * i)
        print(sol)
    else:
        print('NO SOLUTION')