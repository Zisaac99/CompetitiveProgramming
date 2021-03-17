n = int(input())
a = []
a.append(n)
while n != 1:
    if n % 2 ==0:
        n /= 2
    else:
        n = (n*3) + 1
    a.append(int(n))

p = ''
for i in range(len(a)):
    if i != len(a) - 1:
        p += f'{str(a[i])} '
    else:
        p += str(a[i])
print(p)