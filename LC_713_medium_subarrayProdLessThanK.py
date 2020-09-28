
# https://leetcode.com/problems/subarray-product-less-than-k/
def numSubarrayProductLessThanK(self,nums, k):
    def makeSum(n):
        ans = 0
        for i in range(1,n+1):
            ans+=i
        return ans   
    running_sum = 1
    j = 0
    ans = 0
    window_length = 0
    # for every index we need to find a window_length
    for i in range(len(nums)):
        j = max(i, j)
        window_length = max(0,window_length)
        while True:
            # if we are at end of array we can calculate all remaining windows at same time with makeSum() and terminate early
            if j == len(nums):
                ans+=window_length
                return ans + makeSum(window_length-1)      
            # if we are still below k we need to make window bigger 
            if running_sum * nums[j] < k:
                running_sum*=nums[j]
                window_length+=1
                j+=1
            else:
                # we ahve found our window, add answer then reset variables
                ans+=window_length
                # we only remove the first element if our window was more than 1 element, otherwise we still have running_sum of 1
                if i !=j:
                    running_sum = running_sum / nums[i]
                window_length-=1
                break
    return ans