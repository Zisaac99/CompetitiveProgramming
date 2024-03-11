# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        ans = ListNode(0)
        dummyHead = ans
        while l1 or l2 or overflow != 0:
            val1, val2 = 0, 0

            if l1:
                val1 = l1.val
                l1 = l1.next

            if l2:
                val2 = l2.val
                l2 = l2.next

            sum = val1 + val2 + overflow

            if sum >= 10:
                sum = sum - 10
                overflow = 1
            else:
                overflow = 0

            dummyHead.next = ListNode(sum)
            dummyHead = dummyHead.next
        return ans.next
