class Solution():
    def Decode_Strng(self,s):

        stack=[]
        count=0
        currstrg=''

        for i in s:
            if i.isdigit():
                    count=count*10+int(i)

            elif i=='[':
                stack.append(currstrg)
                stack.append(count)
                currstrg=''
                count=0

            elif i==']':
                tmp=stack.pop()
                laststrg=stack.pop()
                currstrg=laststrg + tmp*currstrg


            else:
                currstrg+=i
        return currstrg


first=Solution()
print first.Decode_Strng("3[a2[c]]")

