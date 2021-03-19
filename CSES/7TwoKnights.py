n = int(input())
factorial = 1
for i in range(1,n + 1):
   poss = ((i**2) * ((i**2) - 1))//2 #Identical permutations
   attack = 4 * (i - 1) * (i - 2)
   print(int(poss-attack))