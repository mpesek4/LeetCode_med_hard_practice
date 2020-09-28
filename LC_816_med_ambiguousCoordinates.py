
# https://leetcode.com/contest/weekly-contest-80/problems/ambiguous-coordinates/

def ambiguousCoordinates(S):
    def zeroCheck(s):
        # LIST OF INVALID CASES
        # if there was a decimal and hte last number is 0
        # leadings zeroes before decimal
        s  = "".join(s)
        s = s.split(".")
        
        leftHalf = s[0]
        rightHalf = s[1]
        if len(leftHalf) > 1 and (leftHalf[0] == '0' and rightHalf[0] == '0'):
            return False
        if rightHalf[-1] == '0':
            return False
        return True
    
    def validPermutations(s):
        #this function tries decimals in every location
        # we have to check extraneous zeroes
        ans = 1
        for i in range(1,len(s)):
            s.insert(i,".")
            if zeroCheck(s):
                ans+=1
            del s[i]
        return ans
                     
    s = list(S)
    s = s[1:-1]
    
    answer = 0
    for i in range(1,len(s)):
        left = s[:i]
        right = s[i:]
        
        numLeft = validPermutations(left)
        numRight = validPermutations(right)
        answer+= numLeft * numRight 
    return answer