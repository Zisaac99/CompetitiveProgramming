rocks = 11
arr = [30,70, 75, 120, 160, 170, 180, 190, 200, 246, 258]
hop = 50
next = 0
curr = 0
counter = 0


while(next <= rocks - 1):
    if arr[next] - curr > hop:
        curr = arr[next - 1]
        counter += 1
    else:
        next += 1

counter += 1
print(counter)

        