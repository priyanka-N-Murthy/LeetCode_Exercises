def Merge_lst(l1,l2):

    
    for i in xrange(0,len(l1)):
        for j in xrange(0,len(l2)):
            if (l2[j]-l1[i]==1):
                l1[i+1]=(l2[j])
                #l1.insert(l1[i+1],l2[j])
                i+=1
                j+=1
            elif(l2[j]-l1[i]>1):
                j+=1
    # l1.extend(l2)
    # l1.sort()
    return l1
print Merge_lst([2,5,6,7,9],[3,4,8])
