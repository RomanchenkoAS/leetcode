'''You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        
        for token in tokens:
            # Either it is a number or a minus '-' followed by a number
            if token.isnumeric() or token[1:].isnumeric():
                # print("%s" % token)
                stack.append(int(token))
                
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
                
            elif token == "-":
                _a = stack.pop()
                _b = stack.pop()
                stack.append(_b - _a)
                del _a, _b
                
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
                
            elif token == "/":
                _a = stack.pop()
                _b = stack.pop()
                _result = _b / _a
                
                if _b % _a == 0:
                    stack.append(int(_result))
                elif _result < 0:
                    stack.append(int(_result) + 1)
                else:
                    stack.append(int(_result)) 
                
                del _a, _b, _result

        return stack.pop()
            
s = Solution()

# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["4","-2","/","2","-3","-","-"]

print(s.evalRPN(tokens))