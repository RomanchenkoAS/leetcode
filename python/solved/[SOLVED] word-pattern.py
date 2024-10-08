"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern and not s:
            return True
        words = s.split()
        if len(words) != len(pattern):
            return False

        mapping = {}
        used_words = set()
        for char, word in zip(pattern, words):
            # Main case
            if char in mapping:
                if mapping[char] != word:
                    return False

            # New letter-word pair
            else:
                # To avoid duplicated words in mapping
                if word in used_words:
                    return False

                mapping[char] = word
                used_words.add(word)
        return True


s = "dog cat cat dog"

sol = Solution()
print(sol.wordPattern('abba', s))
