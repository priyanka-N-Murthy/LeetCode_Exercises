# Given an array S of n integers, find a pair of integers in S such that the sum is closest to a given number, target.
# Return the pair of integers.

def Sum_pair(l1,target):
    res=[]
    i=0
    j=len(l1)-1
    if not l1 or not target:
        return []
    while i<j:
        s=l1[i]+l1[j]
        if(s<target):
            i+=1
        elif(s>target):
            j-=1
        elif(s==target):
            res.append(l1[i])
            res.append(l1[j])
            i+=1
            j-=1
    return res
print Sum_pair([1,3,4,4],8)
