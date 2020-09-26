#https://leetcode.com/problems/most-profit-assigning-work/submissions/

# blown away I got this on 1st try (2nd cuz I misread max skill as 10,000 and not 100,000)
def maxProfitAssignment(self,difficulty, profit, worker):
        difficult_mapped_to_idx = {}
        n = len(difficulty)
        max_up_to_idx = [-1 for _ in range(n)]

        diff_profit = []
        # here i just combine 2 arrays into an array of tuples and sort it
        for i in range(n):
            diff_profit_item = (difficulty[i], profit[i])
            diff_profit.append(diff_profit_item)
        diff_profit.sort()


        max_up_to_idx[0] = diff_profit[0][1]
        difficult_mapped_to_idx[diff_profit[0][0]] = 0

        # treating this as a pseudo DP problem/sliding window, in order to not have to search all the jobs a worker at a certain skill levle can do, we store
        # the best job for windows of skills

        # each of these windows goes from 0:idx+1 so if you have a skill lvl of 6, we have precalculated the best job for you in window of 0:6
        for i in range(1,n):
            max_up_to_idx[i] = max(max_up_to_idx[i-1], diff_profit[i][1])
            difficult_mapped_to_idx[diff_profit[i][0]] = i

        prev_diff = diff_profit[0][0]

        # not all skill levels are represented, so this maps nonexistant skill lvls to the previous one we have calculated
        # if your skill lvl is 100 but we only have jobs for 50 and 101, you can only do a window of 0:50
        for i in range(100001):
            if i < prev_diff:
                continue
            if i not in difficult_mapped_to_idx:
                difficult_mapped_to_idx[i] = prev_diff
            else:
                prev_diff = difficult_mapped_to_idx[i]


        answer = 0
        # not we just look up the best job for the skill_lvl of each worker and add it to answer
        for skill_lvl in worker:
            if skill_lvl < diff_profit[0][0]:
                continue
            i = difficult_mapped_to_idx[skill_lvl]
            answer += max_up_to_idx[i]
        return answer