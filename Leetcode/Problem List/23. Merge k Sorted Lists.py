# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##### SOLUTION 1: USING APPEND EACH NODE VALUE INTO ARRAY AND SORTING THE ARRAY BEFORE CONVERTING IT INTO A LINKEDLIST #####
##### TIME COMPLEXITY: O(Nlog(N)) #####
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in range(len(lists)):
            l1 = lists[i]

            while l1:
                arr.append(l1.val)
                l1 = l1.next

        arr.sort()

        ans = ListNode()
        dummyHead = ans
        
        for i in arr:
            dummyHead.next = ListNode(i)
            dummyHead = dummyHead.next
        
        return ans.next
    
##### SOLUTION 2: USING A HEAP #####
##### TIME COMPLEXITY: O(Nlog(K)) #####


class Solution:
    from heapq import heappush, heappop
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i,ll in enumerate(lists):
            if ll:
                heappush(heap,(ll.val,i,ll))# need to add i inside as inn case the heap already has an element with the same priority, 
                                            # Python compares the next element of the tuple. We are enable to compare which ll is smaller
                                            #That is why we need index i in the second place.
        ans = ListNode()                    
        dummyHead = ans
        while heap:
            _,i,curr = heappop(heap)

            if curr.next:
                heappush(heap,(curr.next.val,i,curr.next))

            dummyHead.next = curr
            dummyHead = dummyHead.next
        
        return ans.next
