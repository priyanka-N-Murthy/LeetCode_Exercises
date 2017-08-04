def SimplifyPath(path):
    stack=[]
    s=path.split("/")

    for item in s:
        if item=='.' or item=='':
            pass
        elif item=='..':
            if len(stack)>0:
                stack.pop()
        else:
            stack.append(item)

    return "/" + "/".join(stack)


print SimplifyPath("/home//foo/")