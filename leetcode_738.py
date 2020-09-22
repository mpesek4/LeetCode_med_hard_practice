
# https://leetcode.com/problems/monotone-increasing-digits/
def monotoneIncreasingDigits(N):
        ''' Once we have our num_set with all mono increasing values below 10^9,
        we can binary search for the one that is just below target'''
        def binary_search(N,num_set):
            l = 0
            r = len(num_set)-1

            largest = -1
            while l < r:
                m = (l+r) // 2
                temp = num_set[m]
                if num_set[m] > N:
                    r = m
                else:
                    largest = num_set[m]
                    l = m+1
            return largest

        num_set = [1,2,3,4,5,6,7,8,9]
        dp = {}

        for num in num_set:
            '''add all the digits that maintain the monotone restraint
            then we will backtrack and do the same for newly added numbers, I could have optimized and saved index in numset to not repeat
            instead of using a dictionary to not repeat values, but this was fast enough
            to pass leetcode'''
            last_digit = num % 10
            for i in range(last_digit,10):
                x = num*10+i
                if x < 10**9:
                    if x not in dp:
                        num_set.append(x)
                    dp[x] = 1

        return binary_search(N, num_set)





print(monotoneIncreasingDigits(63))