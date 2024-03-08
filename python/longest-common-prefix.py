class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            if not strs[i].startswith(prefix):
                length = 0
                for char1, char2 in zip(strs[i], prefix):
                    if char1 == char2:
                        length += 1
                    else:
                        break
                if length == 0:
                    return ""
                else:
                    prefix = prefix[:length]
        return prefix


s = Solution()
strs = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))
