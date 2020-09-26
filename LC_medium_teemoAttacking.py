

#https://leetcode.com/problems/teemo-attacking/
def findPoisonedDuration(self,timeSeries, duration):
    
        ''' my solution kinda sucks but they said time wouldn't be over 10k so I just iterated over every time because I thought it'd be easier
        logic than iterating over the specific timeSeries times, turns out the other way is much easier'''
        poison_left = 0
        count = 0

        time_dict = {}
        # one pass for a dict so we don't have to repeatedly search for times
        for time in timeSeries:
            time_dict[time] = 1


        for i in range(0, timeSeries[-1]+1):
            took_poison = False

            # if there is poison left we always take 1 damage and set took_poison to true
            if poison_left > 0:
                count+=1
                poison_left-=1
                took_poison = True
            # if this is a time that we take another poison duration...
            if i in time_dict:

                # poison doesn't stack 
                poison_left = max(duration-1, poison_left)

                # edge case where poison duration is 1 so we need to just take 1 damage
                if duration == 1 and poison_left == 0:
                    count+=1
                    continue
                # edge case for duration  == 0, 
                if poison_left == 0:
                    continue
                count+=1
                # if already took dmg this round this removes double damage taken
                if took_poison == True:
                    count-=1

        count+= poison_left

        return count