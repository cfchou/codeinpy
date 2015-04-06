__author__ = 'cfchou'

# https://leetcode.com/problems/binary-tree-right-side-view/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        ret = []
        stack = []
        if None == root:
            return ret;
        else:
            stack.append(root)

        while 0 != len(stack):
            tmp = []
            rightMost = None
            while 0 != len(stack):
                e = stack.pop()
                rightMost = e.val
                if None != e.left:
                    tmp.append(e.left)
                if None != e.right:
                    tmp.append(e.right)
            ret.append(rightMost)
            tmp.reverse()
            stack = tmp
        return ret

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.right = t5
t3.right = t4
sol = Solution()
print(sol.rightSideView(t1))

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.right = None
t2.left = t4
print(sol.rightSideView(t1))


