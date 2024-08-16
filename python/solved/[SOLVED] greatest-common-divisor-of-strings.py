"""
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""


def is_divisor(s: str, pattern: str) -> bool:
    return s.replace(pattern, "") == ""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ""

        if any(char not in str1 for char in str2):
            return ""

        pattern = []
        possible_gcd = ""

        len1 = len(str1)
        len2 = len(str2)

        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                return ""

            pattern.append(char1)

            # Check if pattern mathematically may be divisor
            if len1 % len(pattern) == len2 % len(pattern) == 0:
                pattern_string = "".join(pattern)
                if is_divisor(str1, pattern_string) and is_divisor(str2, pattern_string):
                    possible_gcd = pattern_string

        return possible_gcd


str1 = "ABABAB"
str2 = "ABAB"
sol = Solution()
res = sol.gcdOfStrings(str1, str2)
print(res)
