"""There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its 
next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # Number of gas stations
        length = len(gas) - 1
        print("length = ", length)

        for i, g in enumerate(gas):
            print(f"\n\nStarting from station #{i} we have {g} in tank")
            
            tank = g

            j = i 
            
            not_enough = False
            while j + 1 != i:
                # current
                tank = tank - cost[j]
                print(f"we spent {cost[j]}, currently in tank {tank}")
                if tank < 0:
                    not_enough = True
                    break
                else:
                    j = j + 1 if j + 1 <= length else 0
                    tank += gas[j]
                    print(f"fill up to {tank}")
                
            if not_enough:
                continue
            elif tank > cost[i-1]:
                return i

        return -1

s = Solution()

# gas = [1,2,3,4,5]
gas = [2,3,4]
# cost = [3,4,5,1,2]
cost = [3,4,3]

print(s.canCompleteCircuit(gas, cost))