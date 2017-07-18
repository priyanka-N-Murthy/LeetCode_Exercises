def Move_items(s,n):
    tmp=[]
    # if s==None or n==None:
    #     return s

    tmp=s.append(n)
    tmp=tmp.sort()

    return tmp
print Move_items([1,2,3],[4])