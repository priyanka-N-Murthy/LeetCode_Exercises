def MergeSorted_Linkdlst(l1,l2):
    res=ListNode(0)
    dummy=res

    while l1!=None and l2!=None:
        if l1.val<l2.val:
            dummy.next=l1
            l1=l1.next
        else:
            dummy.next=l2
            l2=l2.next
        dummy=dummy.next

    if l1!=None:
        dummy.next=l1
    else:
        dummy.next=l2
    return res.next