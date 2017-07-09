def climbStairs(n):

    if (n==0 or n==1 or n==2):
        return n
    fib=[1,2]

    for i in xrange(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]
print climbStairs(5)