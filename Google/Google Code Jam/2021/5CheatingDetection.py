import numpy as np
t = int(input())
p = int(input())
for n in range(t):
    prob = []
    for i in range(100):
        prob.append(((input().count('1')/10000) * 100) - 50)

    idx = prob.index(min(prob))
    print(f'Case #{n + 1}: {idx + 1}')