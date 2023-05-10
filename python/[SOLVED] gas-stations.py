"""There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its 
next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique"""

def sum(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        # Just in case assholes give us >10**3 numbers, we can do a simple yes-no check
        if len(gas) > 1000:
            if sum(gas) < sum(cost):
                return -1

        # Number of gas stations
        length = len(gas) - 1
        
        """ If we go from A and stuck at B then we cannot get to B from any point between A & B"""
        to_skip = set()

        for i, g in enumerate(gas):
            if i in to_skip:
                continue
            
            tank = g
            
            if g == 0:
                continue
            
            j = i 
            tank = tank - cost[j]
            if tank < 0:
                continue
            j = j + 1 if j + 1 <= length else 0
            tank += gas[j]
            
            not_enough = False
            while j != i:
                tank = tank - cost[j]
                if tank < 0:
                    not_enough = True
                    break
                else:
                    j = j + 1 if j + 1 <= length else 0
                    tank += gas[j]
                
            if not_enough:
                # Skip in future all the stations between i and j
                for n in range(i, j):
                    to_skip.add(n)
                continue
            else:
                return i

        return -1