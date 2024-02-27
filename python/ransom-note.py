class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}

        for letter in magazine:
            dictionary.setdefault(letter, 0)
            dictionary[letter] += 1

        for letter in ransomNote:
            if letter not in dictionary:
                return False
            else:
                dictionary[letter] -= 1
                if dictionary[letter] < 0:
                    return False
        return True
