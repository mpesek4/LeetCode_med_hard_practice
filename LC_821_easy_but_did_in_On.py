
#https://leetcode.com/problems/shortest-distance-to-a-character/solution/

def shortestToChar(S, C):
    def binarySearch(myArr,val):
        l = 0
        r = len(myArr)
        
        oneBefore = -1
        while l < r:
            m = (l+r) // 2
            if myArr[m] > val:
                r = m
            else:
                oneBefore = m
                l = m +1
        return oneBefore
    
    indices_of_char = []
    for idx,char in enumerate(list(S)):
        if char == C:
            indices_of_char.append(idx)
    answer = [0 for _ in range(len(S))]
    

    # we looped once to store all indices of target, now we just do a binary search for each index to find two closest targets, take min distance between options
    for idx,char in enumerate(list(S)):
        if char == C:
            answer[idx] = 0
        else:
            oneBefore = binarySearch(indices_of_char, idx)
            if oneBefore == -1:
                answer[idx] = indices_of_char[0]-idx
            else:
                if oneBefore+1 < len(indices_of_char):
                    answer[idx] = min(abs(indices_of_char[oneBefore]- idx), abs(indices_of_char[oneBefore+1]-idx))
                else:
                    answer[idx] = abs(indices_of_char[oneBefore]-idx)
    return answer