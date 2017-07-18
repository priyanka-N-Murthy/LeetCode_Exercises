def add_Ele(l):
    i=0
    count=0
    while i<len(l):
        count+=l[i]
        i+=1
    return count
    res=0
    # for i in xrange(0,len(l)):
    #     res+=l[i]
    # return res
print add_Ele([-1,-2,-4,5])