
#https://leetcode.com/problems/gas-station/

def canCompleteCircuit(self,gas, cost):
        n = len(gas)
        def circuitFromI(i, gas, cost):
            current_gas = gas[i]
            current_idx = i
            count = 0
            # kind of a simple unoptimized simulation algorithm, we just ravel circularly around the area until we fail our condition
            # could optimize this by realizing that if we fail going from a-b, every index in between will fail as well and that would turn it from
            #n^2 to n runtime, but this was accepted as well
            while current_gas >= cost[current_idx]:
                if count == n:
                    return True      
                current_gas-= cost[current_idx]
                current_idx += 1
                current_idx %= n
                current_gas+=gas[current_idx]
                count+=1
            return False


        for i in range(n):
            if circuitFromI(i, gas, cost):
                return i
        return -1