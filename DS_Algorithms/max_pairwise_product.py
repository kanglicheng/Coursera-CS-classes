# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
#a=[4, 3, 2, 5]

if(len(a)<=1):
    print (0)
else:        
    n=len(a)
    a.sort()
    print(max(a[-1]*a[-2], a[0]*a[1]))
'''
a=[4, 5, 6, 7]
b=[1]
c=[]
d=[-4, -5, -6, -5]
maxPairWise(a)
maxPairWise(b)
maxPairWise(c)
maxPairWise(d)
'''

#maxElement=max(a)
#a1=a.pop(a.index(max(a)))
#maxElement2=max(a1)

#print(maxElement*maxElement2)
