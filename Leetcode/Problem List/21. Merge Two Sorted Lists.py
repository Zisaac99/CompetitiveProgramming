class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = [1,2,4] 
l2 = [1,3,4]

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

list1 = llcreator(l1)
llchecker(list1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1 and not list2:
        #     return None

        ans = ListNode()
        dummyHead = ans

        # Check if both List1 and List2 is not empty
        while list1 and list2:
            curr = 0
            if list1.val < list2.val:
                # if the current value of list1 is larger than list2 we set curr as list1
                # and set list1 as the next node 
                curr = list1
                list1 = list1.next
            else:
                # vice versa as the above if the current value of list2 is smaller than list1
                curr = list2
                list2 = list2.next

            # we set the dummyHead next to the list1 or list2 depending which current value is smaller
            # this will work as we will keep overriding the current values of list1 or list2 with the smaller one
            # since our linkedlist we are returning is the sorted one of both list1 and list2
            # once done we go to the next value of list1/list2
            dummyHead.next = curr
            dummyHead = dummyHead.next
        
        # if list1/list2 is empty we set the rest of the linkedlist with the remaining nodes of list1/list
        dummyHead.next = list1 or list2
        # return ans.next as the first node is 0 (our placeholder)
        return ans.next
        