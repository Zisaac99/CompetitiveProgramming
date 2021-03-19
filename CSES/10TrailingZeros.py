n = int(input())
counter = 0
while n >= 5: # Find number of 5s 
    n //= 5 # some numbers may have more than 1 5 so we need to check eg. 25 125 28
    counter += n
print(counter)