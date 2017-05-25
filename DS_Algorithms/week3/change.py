# Uses python3
import sys

def get_change(m):
    #write your code here
    cent, nickel, dime =1, 5, 10
    count=0
    change=[0]*3
    while(m >0):
        change=[m-cent, m-nickel, m-dime]
        m= min(i for i in change if i >=0)
        count+=1
        
    return count
    
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

