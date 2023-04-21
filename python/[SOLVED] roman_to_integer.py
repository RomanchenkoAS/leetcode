''' Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. '''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0

        add = {
            'I':  1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if ('IX') in s:
            sum += 9
            s = s.replace('IX', '')
        if ('IV') in s:
            sum += 4
            s = s.replace('IV', '')

        if ('XL') in s:
            sum += 40
            s = s.replace('XL', '')

        if ('XC') in s:
            sum += 90
            s = s.replace('XC', '')

        if ('CD') in s:
            sum += 400
            s = s.replace('CD', '')

        if ('CM') in s:
            sum += 900
            s = s.replace('CM', '')

        for char in s:
            sum += add[char]

        return sum


sol = Solution()

input = 'IX'

result = sol.romanToInt(input)

print(result)
