def Substring_match(s):
    length=len(s)

    for i in xrange(1,length/2+1):
        if length%i==0:
            temp=[s[ind:ind+i] for ind in range(0,length,i)]
            if all(x==temp[0] for x in temp):
                    return True
    return False


print Substring_match("ababf")

