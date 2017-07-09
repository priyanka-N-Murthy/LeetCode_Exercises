def Pali(s):
    # s=list(s)
    # rev=s[::-1]
    # if(rev==s):
    #     return True
    # else:
    #     return False

    i=0
    j=len(s)-1

    while i<j:
        if(s[i]!=s[j]):
            return False
        elif(s[i]==s[j]):
            i+=1
            j-=1
        return True
print Pali("33")