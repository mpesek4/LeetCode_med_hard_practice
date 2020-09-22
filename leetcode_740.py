
#https://leetcode.com/problems/delete-and-earn/

def deleteAndEarn(nums):
    ''' if we take an element we get to take every occurence of that element, I calculate this total in buckets
  by doing an initial pass (first for loop)'''
    buckets = [0 for _ in range(0,10001)]

    for num in nums:
        count = nums.count(num)
        buckets[num] = count * num

    ''' Here is our dp algo, if we choose an element we get its bucket, but we can't use adjacent buckets, so our
    two options are taking a bucket or skipping'''

    take, skip= 0,0
    for i in range(1, 10001):
            take_i = skip + buckets[i]
            # when we skip, we are allowed to skip again, this is necessary because we need to skip numbers that don't exist in our array
            # skip and take represent the previous values that we store for our subproblems (bottom up DP)
            #previous code used take and skip arrays, easier to understand but waste of space since we only need the previous 2 values to compute next 2

            skip_i = max(take, skip)
            take,skip = take_i,skip_i


    return max(take,skip)

print(deleteAndEarn([8,10,4,9,1,3,5,9,4,10]))

