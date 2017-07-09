def revLinkedList(self,head):
    if head==None or head.next==None:
        return head

    curr=head
    next=curr.next
    prev=None

    while (curr!=None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

