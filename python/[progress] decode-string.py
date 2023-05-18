"""Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square 
brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, you may assume that the original data does
not contain any digits and that digits are only for those repeat numbers, k. For example, 
there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105."""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        def process_substring(substring):
            
            result = ""
            index = 0
            char = substring[0]
            
            while True:
            # for char in substring:
                # print("Element #", index, " = ", char)
                if char.isalpha():
                    result += char
                elif char.isnumeric():
                    # print("Char is a number, ", char)
                    new_substring = ""
                    depth = 1
                    for i in range(index + 2, len(substring)):
                        if substring[i] == '[':
                            depth += 1
                        elif substring[i] == ']':
                            depth -= 1
                        
                        if depth == 0:
                            break
                        else:
                            new_substring += substring[i]
                        
                    # New substring is formed
                    result += process_substring(new_substring) * int(char)
                    
                    
                index += 1
                if index >= len(substring):
                    break
                char = substring[index]
                
            return result
                    
        return process_substring(s)

s = "3[a]2[bc]"
sol = Solution()

print(sol.decodeString(s))