"""
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
"""

def get_tribonacci(prev2: int, prev1:int, prev: int, cur_pos: int, limit: int) -> int:
    tribonacci = sum([prev, prev1, prev2])
    if cur_pos == limit:
        return tribonacci

    return get_tribonacci(prev1, prev, tribonacci, cur_pos + 1, limit)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        else:
            return get_tribonacci(0, 1, 1, 3, n)

n = 10
s = Solution()
res = s.tribonacci(n)
print(res)