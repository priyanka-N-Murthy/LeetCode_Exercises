def LenofLatWrd(s):
    s=s.strip()
    temp=""

    for i in xrange(len(s)-1,-1,-1):
        if(s[i]!=' '):
            temp+=s[i]
            length=len(temp)
        else:
             break
    return length

print LenofLatWrd("I love Jazz!")