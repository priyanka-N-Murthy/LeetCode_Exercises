class Solution():
    def isValid(self, s):
        stack=[]
        dict={")":"(","}":"{","]":"["}

        for item in s:
            if item in dict.values():
                stack.append(item)
            elif item in dict.keys():
                if stack==[]or dict[item]!=stack.pop():
                    return False
            else:
                return stack.pop()
        return not stack

first=Solution()
print first.isValid("][")