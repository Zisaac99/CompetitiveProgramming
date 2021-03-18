n = int(input())
if n < 5:
    if n == 1:
        print('1')
    elif n == 4:
        print('2 4 1 3')
    else:
        print('NO SOLUTION')
else:
    default = '2 4 1 3 5 '
    if n == 5:
        print(default[:len(default) - 1])
    else:
        difference = n - 5
        even = ''
        odd = ''
        if difference % 2 == 0:
            for i in range(1,int((difference/2) + 1)):
                even += str((2 * i) + 4) + ' '
                odd += str((2 * i) + 5) + ' '
        else:
            for i in range(1,int((difference/2) + 1) + 1):
                even += str((2 * i) + 4) + ' '
            for i in range(1,int((difference/2) + 1)):
                odd += str((2 * i) + 5) + ' '
        
        perm = even + default + odd
        print(perm[:len(perm) - 1])
