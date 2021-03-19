n = int(input())
if ((n + 1) % 4 != 0) and (n % 4 != 0):
    print('NO')
else:
    if (n + 1) % 4 == 0:
        ac = int((n + 1)/4) - 1
        setone = '1 2'
        settwo = '3'
        setonen = 2
        for i in range(1,ac + 1):
            num = 4 * i
            setone += f' {num} {num+3}'
            settwo += f' {num+1} {num+2}'
            setonen += 2
        print(f'YES\n{setonen}\n{setone}\n{setonen - 1}\n{settwo}')
    else:
        ac = int((n/4)-1)
        setone = '1 4'
        settwo = '2 3'
        setonen = 2
        for i in range(1,ac + 1):
            num = 1 + (4 * i)
            setone += f' {num} {num+3}'
            settwo += f' {num+1} {num+2}'
            setonen += 2
        print(f'YES\n{setonen}\n{setone}\n{setonen}\n{settwo}')