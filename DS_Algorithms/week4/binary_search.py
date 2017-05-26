# Uses python3
import sys

#iterative version of binary search
def binary_search(a, x):
    left, right = 0, len(a)-1
    while (left <= right):
        mid = left + ((right-left)//2)
        a_mid= a[mid]
        #print (mid)
        if (x == a_mid):
            return mid
        elif ( x < a_mid):
            right=mid-1
        elif(x > a_mid):
            left = mid +1
    return -1
    
        
# def linear_search(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print (binary_search(a, x))
        #print(linear_search(a, x), end = ' ')

# a=[1, 2, 3, 4, 5, 6, 7]
# x= 9
# print binary_search(a, x)


"""
This implementation cannot be used to return the index of the target right? Can
only be used to produce true if target is found false OW. 
Need to add back the index somehow. 
I'm reducing the search space in half each time.
"""

# before:
# def binary_search(a, x):
#     left, right = 0, len(a)-1

# after:
# def binary_search(a, x, left = 0, right = None):
#     if not right:
#         right = len(a)-1
      # modify the recursive calls accordingly
      
      # write your code here
#     if (right < left):
#         return left-1
     # while (left <= right):
    #     mid = (left + right-left)//2
    #     if (x == a[mid]):
    #         return mid             #replace this line with return True
    #     elif ( x < a[mid ]):
    #         a=a[:mid-1]       
    #         return binary_search(a, x)
    #     else:
    #         a=a[mid+1:]
    #         return binary_search(a, x)
#       return True
# print binary_search([1, 2, 3, 4, 5], 5)