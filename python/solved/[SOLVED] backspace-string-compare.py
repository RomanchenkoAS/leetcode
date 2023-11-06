'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.'''


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s1 = []
        t1 = []
        
        for char in s:
            if char == '#' and len(s1) > 0:
                s1.pop()
            elif char != '#':
                s1.append(char)
            else:
                continue
                
        for char in t:
            if char == '#' and len(t1) > 0:
                t1.pop()
            elif char != '#':
                t1.append(char)
            else:
                continue
        return t1 == s1
    
s = Solution()

# input1 = "ab#c"
# input2 = "ad#c"
input1 = "y#fo##f"
input2 = "y#f#o##f"

print(s.backspaceCompare(input1, input2))