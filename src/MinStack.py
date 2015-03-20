__author__ = 'cfchou'

# https://leetcode.com/problems/min-stack/
'''
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.
   push(x) -- Push element x onto stack.
   pop() -- Removes the element on top of the stack.
   top() -- Get the top element.
   getMin() -- Retrieve the minimum element in the stack.
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.ms = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if 0 == len(self.ms):
            self.ms.append(x)
        else:
            m = self.ms[len(self.ms) - 1]
            self.ms.append(min(m, x))
        return x

    # @return nothing
    def pop(self):
        if 0 == len(self.stack):
            return
        self.stack.pop()
        self.ms.pop()
        return

    # @return an integer
    def top(self):
        return self.stack[len(self.stack) - 1]

    # @return an integer
    def getMin(self):
        return self.ms[len(self.ms) - 1]

sol = MinStack()
sol.pop()
sol.push(3)
sol.push(6)
sol.push(1)
sol.push(1)
sol.push(2)
sol.push(4)
sol.push(-5)
print(sol.top())
print(sol.getMin())
sol.pop()
print(sol.top())
print(sol.getMin())
sol.pop()

