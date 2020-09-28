
#https://leetcode.com/contest/weekly-contest-80/problems/ambiguous-coordinates/

def ambiguousCoordinates(S):
    def zeroCheck(s):
        # LIST OF INVALID CASES
        # if there was a decimal and hte last number is 0
        # leadings zeroes before decimal
        s  = "".join(s)
        s = s.split(".")
        
        leftHalf = s[0]
        rightHalf = s[1]
        if len(leftHalf) > 1 and leftHalf[0] == '0':
            return False
        if rightHalf[-1] == '0':
            return False
        return True
    
    def validPermutations(s,curr_half):
        #this function tries decimals in every location
        #and if it is a valid one we add it to l or r, which is given by curr_half
        ans = 0
        if s[0] != '0':
            ans = 1
            curr_half.append(s)
        elif len(s) == 1:
            ans = 1
            curr_half.append(s)
        else:
            ans = 0
        for i in range(1,len(s)):
            temp = s[:]
            temp.insert(i,".")
            if zeroCheck(temp):
                curr_half.append(temp)
                ans+=1
        return ans                    
    s = list(S)
    s = s[1:-1]
    answer = [] 
    #because we don't know where the numbers were split from left right, we try every combo of left halves and right halves by splitting at every index
    for i in range(1,len(s)):
        left = s[:i]
        right = s[i:]
        l = []
        r = [] 
        
        numLeft = validPermutations(left , l)
        numRight = validPermutations(right , r)
        # once we have all the valid permutations we just create the strings as stated in problem description, number of strings is numLeft*numRight (didnt end up using that value)
        for left_item in l:
            for right_item in r:
                temp = "("+"".join(left_item)+", "+"".join(right_item)+")"
                answer.append(temp)
    return answer