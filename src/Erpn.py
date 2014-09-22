__author__ = 'cfchou'

# https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/

'''
from enum import Enum
class Op(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }
        def isInt(x):
            try:
                int(x)
                return True
            except ValueError:
                return False
        lifo = []
        for t in tokens:
            if isInt(t):
                lifo.append(int(t))
            else:
                f = op.get(t)
                r = lifo.pop()
                l = lifo.pop()
                # dividing integer in py2 results in floor division.
                # we uses true division and cast to float
                lifo.append(int(f(float(l), r)))
        return lifo.pop()


tk1 = ["2", "1", "+", "3", "*"]
tk2 = ["4", "13", "5", "/", "+"]
tk3 = ["3","-4","+"]
tk4 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 10 * (6 / ((9 + 3) * -11)) + 17 + 5
sol = Solution()
print(sol.evalRPN(tk4))
