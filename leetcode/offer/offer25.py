class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    p1, p2 = l1, l2
    myhead = ListNode(-1)
    q = myhead
    while  p1 and  p2:
        if p1.val < p2.val:
            q.next = p1
            p1 = p1.next
            q = q.next
        else:
            q.next = p2
            p2 = p2.next
            q = q.next
    while  p1:
        q.next = p1
        p1=p1.next
        q=q.next
        q.next = p2
        p2=p2.next
    return myhead.next

if __name__=='__main__':
    l1=ListNode(1)
    l2=ListNode(2)
    l3=ListNode(4)
    l4=ListNode(5)
    l5=ListNode(6)
    l6=ListNode(7)
    l1.next=l2
    l2.next=l3
    l4.next=l5
    l5.next=l6
    myl=mergeTwoLists(l1,l4)
    while myl:
        print(myl.val)
        myl=myl.next