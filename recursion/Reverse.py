def Reverse(s):
    # rev=s[::-1]
    # return rev

    s=list(s)
    i=0
    j=len(s)-1
    while i<j:
        temp=s[j]
        s[j]=s[i]
        s[i]=temp
        i+=1
        j-=1
    return ''.join(s)
print Reverse("VilasNayak")