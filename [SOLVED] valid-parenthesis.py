#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = []
        
        for char in s:
            if char in '[{(':
                opened += char
            elif (char in ']})'):
                try:
                    l_char = opened.pop()
                except IndexError:
                    return False
                
                if not ((l_char == '[' and char == ']') or (l_char == '{' and char == '}') or (l_char == '(' and char == ')')):
                    return False
            
        # Return True if array is empty and False otherwise
        return not bool(opened)
                
        
solution = Solution()
s = "]"

a = solution.isValid(s)

print(a)