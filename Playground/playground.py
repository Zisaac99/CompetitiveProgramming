import math
nums1 = [1,2,3,5,6]
nums2 = [4]

# m = len(nums1)
# n = len(nums2)

# def solve(start,end):
#     print(f'Start:{start},End:{end}')
#     p1 = (start + end + 1) // 2
#     p2 = ((m + n + 1) // 2) - p1
#     print(f'p1:{p1},p2:{p2}')
#     m_p_left = float('-inf') if p1 == 0 else nums1[p1 - 1]
#     m_p_right = float('inf') if p1 == m else nums1[p1]
#     n_p_left = float('-inf') if p2 == 0 else nums2[p2 - 1]
#     n_p_right = float('inf') if p2 == n else nums2[p2]

#     if m_p_left <= n_p_right and n_p_left <= m_p_right:
#         if (m + n) % 2 == 1:
#             return max(m_p_left,n_p_left)
#         else:
#             return (max(m_p_left,n_p_left) + min(m_p_right,n_p_right)) / 2
#     elif m_p_left > n_p_right:
#         return solve(start, p1 - 1)
#     else:
#         return solve(p1+1, end)

# if m == 0:
#     if n % 2 == 0:
#         print(nums2[(n/2) - 1] + nums2[(n/2)])/2
#     else:
#         print(nums2[n//2])
# elif n == 0:
#     if m % 2 == 0:
#         print(nums1[(m/2) - 1] + nums1[(m/2)])/2
#     else:
#         print(nums1[m//2])
# else:
#     print(solve(0,m-1))

ans = 0
m = len(nums1)
n = len(nums2)

if m > n:
    nums1, nums2 = nums2, nums1
    m, n = n, m

def solve(start,end):
    print(f'Start:{start},End:{end}')
    p1 = (start + end + 1) // 2
    p2 = ((m + n + 1) // 2) - p1
    print(f'p1:{p1},p2:{p2}')

    m_p_left = float('-inf') if p1 == 0 else nums1[p1 - 1]
    m_p_right = float('inf') if p1 == m else nums1[p1]
    n_p_left = float('-inf') if p2 == 0 else nums2[p2 - 1]
    n_p_right = float('inf') if p2 == n else nums2[p2]

    if m_p_left <= n_p_right and n_p_left <= m_p_right:
        if (m + n) % 2 == 1:
            return max(m_p_left,n_p_left)
        else:
            return (max(m_p_left,n_p_left) + min(m_p_right,n_p_right)) / 2
    elif m_p_left > n_p_right:
        return solve(start, p1 - 1)
    else:
        return solve(p1+1, end)
    
if m == 0:
    if n % 2 == 0:
        ans = (nums2[int(n/2) - 1] + nums2[int(n/2)])/2
    else:
        ans = nums2[n//2]
elif n == 0:
    if m % 2 == 0:
        ans = (nums1[int(m/2) - 1] + nums1[int(m/2)])/2
    else:
        ans = nums1[m//2]
else:
    ans = solve(0,m-1)

print(ans)