def NoOfOccurence(s):
    d={}
    res=[]
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print d
    for key,val in enumerate(d):
        if(d[val]>1):
            res.append(val)
    return res


print NoOfOccurence("asljadhiffg")