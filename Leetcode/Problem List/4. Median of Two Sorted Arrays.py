class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        m = len(nums1)
        n = len(nums2)

        # search on the smaller array to optimise O(min(log(m,n)))
        # if we dont do this we will also encounter errors on the two types of movement on an array of size 1
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        def solve(start,end):
            p1 = (start + end + 1) // 2
            p2 = ((m + n + 1) // 2) - p1

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

        # catch empty array case
        if m == 0:
            if n % 2 == 0:
                return((nums2[int(n/2) - 1] + nums2[int(n/2)])/2)
            else:
                return(nums2[n//2])
        elif n == 0:
            if m % 2 == 0:
                return ((nums1[int(m/2) - 1] + nums1[int(m/2)])/2)
            else:
                return(nums1[m//2])
        else:
             return(solve(0,m-1))