t = int(input())
inputs = [list(map(str,input().rstrip().split())) for i in range(t)]
for n in range(t):
    x = int(inputs[n][0])
    y = int(inputs[n][1])
    s = inputs[n][2]
    
    j = s.count('J')
    c = s.count('C')
    filler = s.count('?')

    cost = 0
    if filler == 0:
        cost = (s.count('CJ') * x) + (s.count('JC') * y)
        print(f'Case #{n + 1}: {cost}')
    elif (c > 0 and j == 0 ) or (c == 0 and j > 0) or (c == 0 and j == 0):
        print(f'Case #{n + 1}: 0')
    else:
        s = list(s)
        etr = []
        counter = 0 
        for i in range(len(s)):
            if s[i] == '?' and counter == 0:
                counter += 1
            elif s[i] == '?' and counter == 1:
                etr.append(i)
            elif s[i] != '?' and counter == 1:
                counter = 0
        for i in range(len(etr)):
            s.pop(etr[i] - i)
            
        for i in range(len(s)):
            if s[i] == '?':
                if i - 1 < 0:
                    if s[i + 1] == 'C':
                        s[i] = 'C'
                    else:
                        s[i] = 'J'
                elif i + 1 >= len(s):
                    if s[i -1] == 'C':
                        s[i] = 'C'
                    else:
                        s[i] = 'J'
                else:
                    if (s[i-1] == 'C' and  s[i+1] == 'J') or (s[i-1] == 'J' and  s[i+1] == 'C') or (s[i-1] == 'C' and  s[i+1] == 'C'):
                        s[i] = 'C'
                    else:
                        s[i] = 'J'
        smin = ''.join(s)
        cost = (smin.count('CJ') * x) + (smin.count('JC') * y)
        print(f'Case #{n + 1}: {cost}')