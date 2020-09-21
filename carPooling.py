
# https://leetcode.com/problems/car-pooling/

def carPooling(trips, capacity):

    
    cap_arr = [0 for _ in range(1000)]

''' Iterating over trips, we create a capacity array that stores how many people are added or removed at certain times'''
    cmax = -1
    for idx,trip in enumerate(trips):
        cmax = max(cmax,trip[2])
        cap_arr[trip[2]] -= trip[0]
        cap_arr[trip[1]]+= trip[0]
    current_cap = 0

    ''' Now when we iterate over each time, we keep track of a current total capacity that needs to stay below 'capacity', which is updated with all additions and removals'''
    for i in range(0, cmax+1):
        current_cap+= cap_arr[i]
        if current_cap > capacity:
            return False
    return True

'''runtime O(n) space O(n)   we could also do this in one pass if we sort the array runtime would be nlogn which might be better than our 2 loops'''
print(carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3))