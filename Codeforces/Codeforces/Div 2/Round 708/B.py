t = int(input())
for _ in range(t):
    nm = list(map(int,input().rstrip().split()))
    n,m = nm[0],nm[1]
    a = list(map(int,input().rstrip().split()))
    a_unique = list(sorted(set(a)))
    mdivarray = 0
    divarray = []
    a_unique_notdiv = []
    counter = 0
    for i in a_unique:
        if i % m == 0:
            counter += 1
        else:
            a_unique_notdiv.append(i)
    if counter > 0:
        mdivarray += 1
    if len(a_unique_notdiv) != 0:
        max_a_unique_notdiv = max(a_unique_notdiv)
        ii = (max_a_unique_notdiv - (max_a_unique_notdiv % m)) / m
        while len(a_unique_notdiv) != 0:
            currentNumber = a_unique_notdiv[0]
            for j in reversed(range(1,int(ii + 2))):
                nn = ((m * j) - currentNumber)
                if nn in a_unique_notdiv and nn != currentNumber:
                    a_unique_notdiv.remove(currentNumber)
                    a_unique_notdiv.remove(nn)
                    
                    fcount = a.count(currentNumber) 
                    scount = a.count(nn)
                    if abs(fcount - scount) > 1:
                        if currentNumber % m == 0 or nn % m == 0:
                            mdivarray += 1
                        else:
                            mdivarray += 2
                    else:
                        mdivarray += 1
                    break
            if a_unique_notdiv.count(currentNumber) != 0:
                a_unique_notdiv.remove(currentNumber)
                mdivarray += 1
    
    print(mdivarray)
    
        



