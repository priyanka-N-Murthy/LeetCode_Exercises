def RemDuplicates(n):
    res=[]
    for i in xrange(0,len(n)):
        if n[i] not in res:
            res.append(n[i])
    return res
print RemDuplicates([1,1,1,1,1,0])