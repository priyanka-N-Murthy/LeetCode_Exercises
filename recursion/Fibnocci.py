def fibnocci(num):
    first=0
    second=1
    res=[]
    i=0
    if num==0:
        return first
    elif num==1:
        return second
    elif num==2:
        return first+second
    else:
        i=3
        res.append(first)
        res.append(second)
        while i<=num:
            temp=first+second
            res.append(temp)
            first=second
            second=temp
            i+=1

        return res
#     first=0
#     second=1
#     if num<0:
#         print "Invalid sequence number"
#     elif num==0:
#         print first
#     elif num==1:
#         print second
#     elif num==2:
#         print first+second
#     else:
#         count=3
#         print first
#         print second
#         while(count<=num):
#             seq=first+second
#             first=second
#             second=seq
#             count+=1
#             print seq
# fibnocci(7)
print fibnocci(4)