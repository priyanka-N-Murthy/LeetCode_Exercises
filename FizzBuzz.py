def fizzBuzz(n):
    res=[]
    i=1
    while i<=n:
        if(i%2==0 and i%3!=0):
            res.append("Fizz")
        elif(i%3==0 and i%2!=0):
            res.append("Buzz")
        elif(i%2==0 or i%3==0):
            res.append("FizzBuzz")
        else:
            res.append(i)
        i+=1
    return res
print fizzBuzz(20)