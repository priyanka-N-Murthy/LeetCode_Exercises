def NestedIterator(s):
    stack=[]

    for sublist in s:
        if isinstance(sublist,list):
            for item in sublist:
                stack.append(item)
        else:
            stack.append(sublist)

    return stack
print NestedIterator([[9,6],0,[4],[1,5,8,2]])