# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow , fast = head, head

        # let fast start at n nodes ahead of slow
        for _ in range(n):
            fast = fast.next

        # if fast is empty we just return the 2nd node onwards,
        # as this would mean that n == the length of ListNode so we need to remove the first element
        if not fast:
            return head.next
        
        # check if the next node of fast is empty
        # if it is empty that means we have reached the last node
        # and slow has reached the n + 1 nodes before the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # rewrite slow next with the n - 1 element
        slow.next = slow.next.next
        return head