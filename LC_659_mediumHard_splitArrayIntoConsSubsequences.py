
# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/split-array-into-consecutive-subsequences/

import copy
def isPossible(nums): 
    def isValid(answer):
        for element in answer:
            if len(element) < 3:
                return False
        return True
    
    def rec(rem_nums, splits, answer):
        if len(rem_nums) == 0:
            if isValid(answer):
                return True
            else:
                return False       
        temp = list(map(str,rem_nums))
        x = "".join(temp)
        if x in explored:
            return False
        
       
        dp[x] = True
        
        for i in range(splits):
            temp = copy.deepcopy(answer)
            if len(temp[i]) == 0 or rem_nums[0] == temp[i][-1] + 1:
                temp[i].append(rem_nums[0])
                x = rec(rem_nums[1:], splits, temp)
                if x == True:
                    return True
        return False
    cmax = -1
    dp = {}
    for num in nums:
        if num in dp:
            dp[num] +=1
        else:
            dp[num] = 1
            
        cmax = max(cmax, dp[num])
    explored = {}
    answer = [[] for _ in range(cmax)]
    
    return rec(nums, cmax, answer)