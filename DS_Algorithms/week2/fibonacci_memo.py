# Uses python3
def calc_fib(n):
    fibTable=[0]*(n+1)
    if (n <= 1):
        return n
    fibTable[0]=0
    fibTable[1]=1
    
    for i in range(2,n+1):
        fibTable[i]=fibTable[i-1]+fibTable[i-2]
    return fibTable[n]

n = int(input())
#n=10
print(calc_fib(n))
