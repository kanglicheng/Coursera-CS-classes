# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    finalValue = 0
    a=0
    A=[0]*len(weights)
    # write your code here
    densities = sorted([[values[i] /float( weights[i]), weights[i]] for i in range(len(weights))], reverse=True)
    
    #while (capacity >0 and densities):
    for i, v in enumerate(densities):
        a= min(capacity, densities[i][1])
        #print(a)
        finalValue += a*densities[i][0]
        capacity -= a
        if (capacity <= 0):
            break
    

    return finalValue
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# weights=[30]
# capacity=1000
# values=[500]

# print (get_optimal_value(capacity, weights, values))