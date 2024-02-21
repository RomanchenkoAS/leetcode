class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            if s[0] == " ":
                return 0
            else:
                return 1
        word_started = False
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if not word_started and s[i] == " ":
                continue
            elif not word_started and s[i].isalpha():
                word_started = True
                length += 1
            elif word_started and s[i] == " ":
                break
            else:
                length += 1
        return length


S = Solution()
input_line = "a"
print(S.lengthOfLastWord(input_line))
