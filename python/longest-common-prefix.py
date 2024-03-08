class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs.pop(0)

        for str in strs:
            if not str.startswith(prefix):
                length = 0
                for char1, char2 in zip(str, prefix):
                    if char1 != char2:
                        break
                    length += 1

                if length == 0:
                    return ""

                prefix = prefix[:length]

        return prefix


s = Solution()
strs = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))
