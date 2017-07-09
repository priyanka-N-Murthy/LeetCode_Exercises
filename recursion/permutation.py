# def permute(self,nums):
#
#     length=len(nums)
#     res=[]
#     first=[]
#     if nums==0 or length==1:
#         return nums
#
#     if length==1:
#         res.append(nums)
#         return res
#
#     if length==2:
#         res.append(nums)
#         swap=nums[1:2]+nums[0:1]
#         res.append(swap)
#
#     tempstrg=nums
#     # #if length>2:
#     for i in xrange(0,length):
#         first=tempstrg[0:1]
#         sublist=self.permute(tempstrg[1:length])
#         for j in xrange(0,len(sublist)):
#             res.append(first+sublist[j])
#         tempstrg=tempstrg[1:length]+tempstrg[0:1]
#     return res
# print permute(1,[1,2,3])

def Combo(inputstrng):
    list=[]
    length=len(inputstrng)


    if length==0:
        return list

    if length==1:
        list.append(inputstrng)
        return list

    if length==2:
        list.append(inputstrng)
        temp = inputstrng[1:2]+inputstrng[0:1]
        list.append(temp)
        return list

    tempstr=inputstrng
    for i in range(0,length):
        first=[tempstr[0]]
        #print first
        sublist=Combo(tempstr[1:length])#Calling its own function
        for j in range(0,len(sublist)):
            list.append(first+sublist[j])
            #print list
        tempstr = [tempstr[1:length]] + [tempstr[0]]
    return list
print Combo([1,2,3])