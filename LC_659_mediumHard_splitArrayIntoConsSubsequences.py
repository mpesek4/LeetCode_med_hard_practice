
# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/split-array-into-consecutive-subsequences/

import copy
# prev answer was not a good DP solution, checking way too many comboes even with some pruning

# here is the greedy approach


def isPossible(self,nums):
        # this function checks a segment of numbers
        # example: if we are checking a val of 4, we want to greedily add to any subsequence that ends in 3 that has a length of 1, and then calculate how many new
        # subsequences will start with 4
        # The number of subsequences that start with 4 depends on how many subsequences we terminated with 3, so it is just freq[i]-freq[i-1]

        # we fail our check if the number of subsequences ending in 3 (ones[3]+twos[3] rep these sequences with length of 1 and 2) is greater than the frequency of 4
        # we also fail if at the end we couldn't append to our subsequences of length one of two, because the requirement is that they are min length 3
        def isValid(nums, l, r):
            n = nums[r]-nums[l]+1

            freq = [0 for _ in range(n+1)]
            ones = [0 for _ in range(n+1)] # number of subsequences of length one ending with value i-1
            twos = [0 for _ in range(n+1)] # number of subsequences of length two ending with value i-1

            for i in range(l,r+1): # frequency of each number in our original array
                freq[nums[i]-nums[l]]+=1 # since we are doing a chunk of our original array, we map our indexes to start at 0 instead of our initial index 
                                                # so that we can keep track of our new array logic with easier indexing, so if 5 is the first value of our array
                                                # it will actually be index 0, and 6 would be index 1 ...etc etc

            for i in range(n):
                if freq[i] < ones[i] + twos[i]: # if we have subsequences that are ending at i-1, we are required to add to them
                    return False
                twos[i+1] = ones[i] # always append to our ones first, so twos are now what previous ones were
                ones[i+1] = max(0,freq[i]- freq[i-1]) # ones is the left over values we couldn't append
            
            return ones[n] == 0 and twos[n] == 0 # after iterating we can't have any sequences with length one or 2
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] - nums[i-1] > 1: # keeping track of chunks of consecutive integers
                if not isValid(nums,k,i-1):
                    return False
                k = i
        return isValid(nums,k,n-1) # last chunk 