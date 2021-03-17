n = input()
m = 0
mr = 0
ccc = ''
for i in n:
    if i != ccc:
        if m > mr:
            mr = m
        ccc = i
        m = 1 
    else:
        m += 1
if m > mr:
    print(m)
else:
    print(mr)
