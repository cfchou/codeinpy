__author__ = 'cfchou'

# https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if None == root:
            return
        self.flattenedEnd(root)
        return
    def flattenedEnd(self, root):
        if None == root.left and None == root.right:
            return root
        if None == root.left:
            endr = self.flattenedEnd(root.right)
            return endr
        else:
            endl = self.flattenedEnd(root.left)
            if root.right:
                endr = self.flattenedEnd(root.right)
                endl.right = root.right
                root.right = root.left
                root.left = None
                return endr
            else:
                root.right = root.left
                root.left = None
                return endl

def printRight(root):
    if root:
        print(root.val)
        printRight(root.right)

t2 = TreeNode(2)
t2.left = TreeNode(3)
t2.right = TreeNode(4)
t5 = TreeNode(5)
t5.right = TreeNode(6)
t1 = TreeNode(1)
t1.left = t2
t1.right = t5

printRight(t1)

sol = Solution()
sol.flatten(t1)

printRight(t1)




