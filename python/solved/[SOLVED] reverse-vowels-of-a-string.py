"""
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']


class Solution:
    def reverseVowels(self, s: str) -> str:
        mapping = []
        for char in s:
            if char.lower() in VOWELS:
                mapping.append(char)

        res = ""
        for char in s:
            if char.lower() in VOWELS:
                res += mapping.pop()
            else:
                res += char
        return res


s = "hello"
sol = Solution()
res = sol.reverseVowels(s)
print(res)
