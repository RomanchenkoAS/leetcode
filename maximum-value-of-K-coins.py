# There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

# In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

# Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, 
# and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k 
# coins optimally.

import itertools
import copy

class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        permutations = itertools.combinations_with_replacement('0123456', k)

        max = 0
        for comb in permutations:
            print(comb)
            copied = copy.deepcopy(piles)
            
            try:
                sum = 0
                for i in comb:
                    pop = copied[int(i)].pop(0)
                    sum += pop
                    # print(f'Adding to a sum {pop}, sum = {sum}')
                
                if sum > max:
                    max = sum
                    # print(f'New max = {max}')
            except IndexError:
                # print(f'Continue')
                continue
                
        return max
        

k = 25
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]

# input = [list1, list2, list3]

piles = [[80,62,78,78,40,59,98,35],[79,19,100,15],[79,2,27,73,12,13,11,37,27,55,54,55,87,10,97,26,78,20,75,23,46,94,56,32,14,70,70,37,60,46,1,53]]

# piles = [[1,100,3],[7,8,9]]


permutations = itertools.combinations_with_replacement('0123456', k)

max = 0
for comb in permutations:
    # print(comb)
    copied = copy.deepcopy(piles)
    
    try:
        sum = 0
        for i in comb:
            pop = copied[int(i)].pop(0)
            sum += pop
            # print(f'Adding to a sum {pop}, sum = {sum}')
        
        if sum > max:
            max = sum
            print(f'New max = {max}')
            print(comb)
    except IndexError as _ex:
        # print(f'Continue, error = ', _ex)
        continue
        