"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""

class Solution(object):
    variants = []
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        list = []
        
        def generate(left, right, s):
            if len(s) == 2 * n:
                list.append(s)
                return
            
            else:
                if left < n:
                    generate(left + 1, right, s + "(")
                
                if  right < left:
                    generate(left, right + 1, s + ")")
                    
        generate(0, 0, "")
        
        return list
            
            
            
        
        
s = Solution()

n = 3

s.generateParenthesis(n)