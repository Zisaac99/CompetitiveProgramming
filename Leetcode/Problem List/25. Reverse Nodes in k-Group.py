class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = [1,2,3,4,5]

def llcreator(list):
    ans = ListNode()
    head = ans
    for i in list:
        head.next = ListNode(i)
        head = head.next
    return ans.next

def llchecker(ll):
    while ll:
        print(ll.val)
        ll = ll.next


##### Recursive Method #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            
            curr = curr.next

        prev = None
        curr = head

        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head.next = self.reverseKGroup(curr,k)
        return prev
    
        
##### Iterative Method #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        def check(c,k):
            for _ in range(k):
                if not c:
                    return 'No'
                c = c.next
            return c

        curr = dummy.next
        first = dummy
        while check(curr,k) != 'No':
            prev = check(curr,k)
            initial = curr
            for _ in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            first.next = prev
            first = initial
            

        return dummy.next

