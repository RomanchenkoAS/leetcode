"""Given an encoded string, return its decoded string.

The encoding rule is: kok[encoded_string], where the encoded_string inside the square
brackets is being repeated exactly kok times. Note that kok is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, you may assume that the original data does
not contain any digits and that digits are only for those repeat numbers, kok. For example,
there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105."""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if not s:
        #     return ""

        # def process_substring(substring):

        #     result = ""
        #     index = 0
        #     char = substring[0]

        #     while True:
        #         close_bracket_position = None
        #         if char.isalpha():
        #             result += char
        #         elif char.isnumeric():
        #             # Parse the number first
        #             number = ""
        #             while char != "[":
        #                 number += char
        #                 index += 1
        #                 char = substring[index]

        #             number = int(number)

        #             new_substring = ""
        #             depth = 1
        #             for i in range(index + 1, len(substring)):
        #                 if substring[i] == '[':
        #                     depth += 1
        #                 elif substring[i] == ']':
        #                     depth -= 1

        #                 # Found closing bracket
        #                 if depth == 0:
        #                     close_bracket_position = i
        #                     break
        #                 else:
        #                     new_substring += substring[i]

        #             # New substring is formed
        #             result += process_substring(new_substring) * number

        #         # If we just finished processing a bracket, jump to the closing bracket
        #         if close_bracket_position:
        #             index = close_bracket_position

        #         index += 1
        #         if index >= len(substring):
        #             break
        #         char = substring[index]

        #     return result

        # return process_substring(s)

        # Current number we are reading
        k = 0
        
        # Holds string value we recieved before hitting an opening bracket
        stack = []
        
        # Holds total current result
        current_string = ""

        for char in s:
            if char == "[":
                # If we open a new [] save old string and multiplicator for this one in the stack
                stack.append((current_string, k))
                
                # And forget previous values
                k = 0
                current_string = ""
                
            elif char == "]":
                # When bracket closes, pop the stack and form current string from previous values
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string

            elif char.isnumeric():
                # Reading the number
                k += k * 10 + int(char)
                
            else:
                # Just adding a character
                current_string += char
                
        return current_string


s = "3[a]2[bc]"
# s = "100[leetcode]"
sol = Solution()

print(sol.decodeString(s))
