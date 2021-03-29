tnq = list(map(int,input().rstrip().split()))
t = tnq[0]
n = tnq[1]
q = tnq[2]
for m in range(t):
    arr = []
    for i in range(n - 2):
        first = 1 + i
        second = 2 + i
        third = 3 + i
        print(f'{first} {second} {third}',flush = True)
        mediann = int(input())
        if mediann == first:
            median = first
        elif mediann == second:
            median = second
        else:
            median = third
        if i == 0:
            if median == 1:
                arr.append(2)
                arr.append(1)
                arr.append(3)
            elif median == 2:
                arr.append(1)
                arr.append(2)
                arr.append(3)
            else:
                arr.append(1)
                arr.append(3)
                arr.append(2)
        else:
            if median == third:
                first_index = arr.index(first)
                second_index = arr.index(second)
                if first_index < second_index:
                    smallerindex = first_index
                else:
                    smallerindex = second_index
                arr.insert(smallerindex + 1,median)
            else:
                if median == first:
                    x = median
                    y = second
                else:
                    x = median
                    y = first
                if arr.index(x) < arr.index(y):
                    arr.insert(0,third)
                else:
                    arr.insert(len(arr),third)
    solution = ''
    for i in range(len(arr)):
        if i != len(arr) - 1:
            solution += str(arr[i]) + ' '
        else:
            solution += str(arr[i])
    print(reversed(solution),flush = True)
    valid = int(input())
    if valid == -1:
        break

                    
            
