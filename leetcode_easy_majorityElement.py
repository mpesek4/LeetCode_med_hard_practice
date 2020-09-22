
# easy warmup problem
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) // 3
        
        dp = {}
        ans = []
        for num in nums:
            if num not in dp:
                dp[num] = 1
            else:
                dp[num] +=1
            if dp[num] == n+1:
                ans.append(num)
         
        return ans


print( majorityElement([2,2]))