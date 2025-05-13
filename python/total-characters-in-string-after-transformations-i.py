import code
from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        letters = defaultdict(int)

        for character in s:
            letters[character] += 1

        for _ in range(t):
            num_z = 0
            if 'z' in letters:
                num_z, letters['z'] = letters['z'], 0

            for i in range(len(ascii_lowercase) - 2, -1, -1):
                key = ascii_lowercase[i]
                if key not in letters:
                    continue

                num_key, letters[key] = letters[key], 0

                new_key = ascii_lowercase[i + 1]
                letters[new_key] = num_key

            if num_z > 0:
                letters['a'] += num_z
                letters['b'] += num_z

        return sum(letters.values()) % (10**9 + 7)


sol = Solution()
t = 2
s = "abcyy"

print(sol.lengthAfterTransformations(s, t))
