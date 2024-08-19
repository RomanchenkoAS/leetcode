"""
443. String Compression
Given an array of characters chars, compress it using the following algorithm:
- Begin with an empty string s. For each group of consecutive repeating characters in chars:
    - If the group's length is 1, append the character to s.
    - Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character
array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""
from typing import List, Optional


class Solution:
    def addSequence(self, char: Optional[str], count: int, chars: List[str], cursor: int) -> int:
        chars[cursor] = char
        if count <= 1:
            return 1
        else:
            prefix = str(count)

            for digit in prefix:
                cursor += 1
                chars[cursor] = digit
            return len(prefix) + 1

    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        cursor = 0  # Where we type next element
        current_character = None
        sequence_length = 0

        for char in chars:
            if char == current_character:
                sequence_length += 1
                continue

            if current_character is not None:
                added_chars = self.addSequence(current_character, sequence_length, chars, cursor)
                cursor += added_chars

            current_character = char
            sequence_length = 1

        added_chars = self.addSequence(current_character, sequence_length, chars, cursor)
        cursor += added_chars
        return cursor


chars = ["a", "a", "b", "b", "c", "c", "c"]
sol = Solution()
res = sol.compress(chars)
print(chars)
print(res)
