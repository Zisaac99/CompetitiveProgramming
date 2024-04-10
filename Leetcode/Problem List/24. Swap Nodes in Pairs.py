class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = [1,2,3,4]

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

head = llcreator(l1)


dummy = ListNode()
dummy.next = head

curr = dummy

while curr.next and curr.next.next:
    first = curr.next
    second = curr.next.next

    first.next = second.next
    second.next = first
    curr.next = second
    curr = curr.next.next

llchecker(dummy.next) 


