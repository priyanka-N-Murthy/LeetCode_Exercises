def itos(num):
    string=''
    i=0
    while num:
        n=num%10
        temp=str(n*(10**i))
        temp=temp[0:1]
        string+=temp
        num=num/10
        i+=1
    string=string[::-1]
    return string
print itos(645673245823)