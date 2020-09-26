
#https://leetcode.com/problems/friends-of-appropriate-ages/

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
    for key in count_dict.keys():
        ans = 0
        if key <= (.5 * key + 7):
            continue
        ans = sum_range(count_dict[key])
        answer+=ans
            
    
    for idx,age in enumerate(ages):
        r = n -1
        while r > idx:
            if ages[r] <= (.5 * age +7):
                r-=1
            else:
                answer+= r-idx
                break
    return answer


def numFriendRequests(self, ages):
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