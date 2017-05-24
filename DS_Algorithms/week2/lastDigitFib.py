# Uses python3
def lastDigitFib(n):
   # memo= [0] * (n+1)
    if (n<=1):
        return n
    first=0
    second=1
    
    for i in range(2, n+1):
        current= (first + second) % 10
        first=second
        second=current
    return current
    
n=int(input())
print (lastDigitFib(n))