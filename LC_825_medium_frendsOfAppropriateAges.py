
#https://leetcode.com/problems/friends-of-appropriate-ages/


# O(nlogn) passes all cases

def numFriendRequests(ages):
    def sum_range(n):
        ans = 0
        for i in range(1,n):
            ans+=i
        return ans

    ages.sort(reverse = True)
    n = len(ages)
    
    answer = 0
    
    count_dict = {}
    for age in ages:
        if age not in count_dict:
            count_dict[age] = 1
        else:
            count_dict[age] += 1
    # this loop handles duplicates because ppl of same age request eachother twice
    for key in count_dict.keys():
        ans = 0
        if key <= (.5 * key + 7):
            continue
        ans = sum_range(count_dict[key])
        answer+=ans

    # sliding window, I coulda done the above logic in this loop as well but this is easier to look at
    # increase j until we can add all the friend requests for i in our window     
    j = 0
    for i in range(1,n):
        while i > j and ages[i] <= .5 * ages[j] + 7:
            j+=1
        answer+= i-j

    return answer # O(nlogn) because we need to sort our array


def numFriendRequests(self, ages): # here is the O(A^2) solution they give which is probably more elegant than what I wrote, since ages is so constrained this is better than O(nlogn)
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA
        return ans
            

            
print(numFriendRequests([6,6]))