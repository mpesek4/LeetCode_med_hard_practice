
# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/find-k-closest-elements/

def findClosestElements(arr, k, x):
    # first 2 functions are just helper methods to return the closest value to a target (favoring smaller elements in case of a tie)
    def getClosest(v1,v2,target):
        if target - arr[v1]> arr[v2] - target:
            return v2
        else:
            return v1
        
    def binarySearch(arr, val):
        if val < arr[0]:
            return 0
        if val > arr[-1]:
            return len(arr)-1
        l = 0
        r = len(arr)
        
        while l < r:
            m = (l+r) // 2        
            if arr[m] > val:  
                if m > 0 and val > arr[m-1]:
                    return getClosest(m-1,m,val)
                r = m
            elif arr[m] == val:
                return m
            else:
                if m < len(arr)-1 and val < arr[m+1]:
                    return getClosest(m, m+1, val)
                l = m + 1
        if abs(arr[m]-k) < abs(arr[m-1]-k):
            return m
        elif abs(arr[m]-k) > abs(arr[m+1]-k):
            return m+1
        else:
            return m-1
      
    closest = binarySearch(arr, x)
    
    r=-1
    l = closest
  
    
    if closest + 1 < len(arr):
        r = closest + 1
   
            
    answer = []

    # Now we use a 2 pointer approach, we keep checking wehether the next left or next right element is closer and update answer and our pointers accordingly
    while k > 0:
        # the negative one checks let us know we no longer have elements to one side, so we just add the remaining k elements from the other side,
        # no other checks needed because they said a solution is guaranteed to exist
        if l == -1:
            answer.append(arr[r])
            k-=1
            r+=1
            continue
        if r == -1:
            answer.append(arr[l])
            k-=1
            l-=1
            continue
        if abs(arr[l]- x) > abs(arr[r] - x):
            answer.append(arr[r])
            k-=1
            r+=1
            if r == len(arr):
                r = -1
        else:
            answer.append(arr[l])
            k-=1
            l-=1
    answer.sort()
    return answer