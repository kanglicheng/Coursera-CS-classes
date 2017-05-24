# Uses python3
import sys

def gcdEuclid(a, b):
    if (b ==0):
        return a
    elif (a==0):
        return b
    aRemainder= a % b
    return gcdEuclid(b, aRemainder)
   

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcdEuclid(a, b))

#print gcdEuclid(104354666, 4333246)