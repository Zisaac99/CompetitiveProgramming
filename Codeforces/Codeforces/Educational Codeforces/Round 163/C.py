# t = int(input())
# for _ in range(t):
#     n = int(input())
    
#     arr = []
#     arr.append(list(input()))
#     arr.append(list(input()))
    
#     target = (1,n-1)
#     ans = 'NO'
#     queue = []
#     visited = set()
#     dir1 = [[0,1],[1,0]]
#     dir2 = [[0,1],[-1,0]]
#     queue.append((0,0))
    
#     while queue:
#         curr = queue.pop(0)
#         x,y = curr
#         if curr not in visited:
#             visited.add(curr)
#             if curr == target:
#                 ans = 'YES'
#                 break
            
#             if (x + y) % 2 == 0:

#                 if x == 0:
#                     dir = dir1
#                 else:
#                     dir = dir2

#                 for x2,y2 in dir:
#                     queue.append((x + x2,y + y2))
#             else:
#                 if arr[x][y] == '>':
#                     queue.append((x,y + 1))
#                 else:
#                     queue.append((x,y - 1))
#     print(ans)

t = int(input())
for _ in range(t):
    n = int(input())
    
    arr = []
    arr.append(list(input()))
    arr.append(list(input()))
    
    ans = 'NO'
    
    target = (1,n-1)
    queue = []
    visited = set()
    queue.append((0,0))
 
    while queue:
        curr_index = queue.pop(0)
        if curr_index == target:
            ans = 'YES'
            break
        else:
            next = []
            if curr_index[0] == 0:
                next = [(1,curr_index[1]),(0,curr_index[1]+1)]
            else:
                next = [(0,curr_index[1]),(1,curr_index[1]+1)]
 
            for i in next:
                #print(f'Current: {curr_index} , Next: {i} , Arrow: {arr[i[0]][i[1]]}, Potential Next: {(i[0],i[1]+1)}')
                if i not in visited:
                    visited.add(i)
                    if i == target:
                        ans = 'YES'
                        break
                    if arr[i[0]][i[1]] == '>':
                        visited.add((i[0],i[1]+1))
                        queue.append((i[0],i[1]+1))
                    
                
    print(ans)