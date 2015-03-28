__author__ = 'cfchou'

# https://leetcode.com/problems/recover-binary-search-tree/
'''
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

A solution using O(n) space is pretty straight forward. Could you devise a
constant space solution?

Input: {68,41,#,-85,#,-73,-49,-98,#,#,#,-124}
Expected: {68,41,#,-73,#,-85,-49,-98,#,#,#,-124}
'''



# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        t1 = self.inorder(root)
        t2 = self.inorderReversed(root)
        if None == t1 and None == t2:
            return
        assert(None != t1 and None != t2)
        tmp = t1.val
        t1.val = t2.val
        t2.val = tmp
        return

    def inorder(self, root):
        stack = []
        cur = root
        prev_val = None
        prev_tree = None
        while None != cur:
            stack.append(cur)
            while None != cur.left:
                cur = cur.left
                stack.append(cur)
            assert(None == cur.left)
            while True:
                cur = stack.pop()
                # visit cur
                if None == prev_val or cur.val >= prev_val:
                    prev_val = cur.val
                    prev_tree = cur
                else:  #cur.val < prev_val
                    return prev_tree

                if None != cur.right:
                    cur = cur.right
                    break
                if 0 == len(stack):
                    return None
        return None

    def inorderReversed(self, root):
        stack = []
        cur = root
        prev_val = None
        prev_tree = None
        while None != cur:
            stack.append(cur)
            while None != cur.right:
                cur = cur.right
                stack.append(cur)
            assert(None == cur.right)
            while True:
                cur = stack.pop()
                # visit cur
                if None == prev_val or cur.val <= prev_val:
                    prev_val = cur.val
                    prev_tree = cur
                else:  # cur.val > prev_val
                    return prev_tree

                if None != cur.left:
                    cur = cur.left
                    break
                if 0 == len(stack):
                    return None
        return None

    def dfsInOrder(self, root):
        stack = []
        cur = root
        while None != cur:
            stack.append(cur)
            while None != cur.left:
                cur = cur.left
                stack.append(cur)
            assert(None == cur.left)
            while True:
                cur = stack.pop()
                self.visit(cur)
                if None != cur.right:
                    cur = cur.right
                    break
                if len(stack) == 0:
                    return
        return

    def dfsInOrderReversed(self, root):
        stack = []
        cur = root
        while None != cur:
            stack.append(cur)
            while None != cur.right:
                cur = cur.right
                stack.append(cur)
            assert(None == cur.right)
            while True:
                cur = stack.pop()
                self.visit(cur)
                if None != cur.left:
                    cur = cur.left
                    break
                if len(stack) == 0:
                    return
        return

    def dfsPreOrder(self, root):
        stack = []
        cur = root
        while None != cur:
            self.visit(cur)
            stack.append(cur)
            while None != cur.left:
                cur = cur.left
                self.visit(cur)
                stack.append(cur)
            while True:
                cur = stack.pop()
                if None != cur.right:
                    cur = cur.right
                    break
                if len(stack) == 0:
                    return
        return

    def dfsPostOrder(self, root):
        stack = []
        cur = root
        while None != cur:
            stack.append(cur)
            while None != cur.left:
                cur = cur.left
                stack.append(cur)
            assert(None == cur.left)
            while True:
                if None != cur.right:
                    cur = cur.right
                    break
                cur = stack.pop()
                self.visit(cur)
                if len(stack) == 0:
                    return
        return

    def visit(self, tree):
        print(tree.val)
        return

    def run(self, root):
        self.dfsInOrder(root)
        print("---------")
        sol.recoverTree(root)
        sol.dfsInOrder(root)
        return

'''
Input: {68,41,#,-85,#,-73,-49,-98,#,#,#,-124}
Expected: {68,41,#,-73,#,-85,-49,-98,#,#,#,-124}
'''

sol = Solution()
t68 = TreeNode(68)
t41 = TreeNode(41)
t73 = TreeNode(-73)
t85 = TreeNode(-85)
t49 = TreeNode(-49)
t98 = TreeNode(-98)
t124 = TreeNode(-124)

t68.left = t41
t41.left = t85
t85.left = t73
t85.right = t49
t73.left = t98
t98.left = t124

sol.run(t68)

print("-------------------------------")
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t3
t2.right = t1
sol.run(t2)

print("-------------------------------")

t1 = TreeNode(1)
t2 = TreeNode(2)
t1.left = t2
sol.run(t1)

print("-------------------------------")
sol.run(TreeNode(0))


# sol.dfsInOrderReversed(t68)
# print("---------")
# sol.dfsInOrder(t68)
# print("---------")
# sol.dfsPreOrder(t68)
# print("---------")
# sol.dfsPostOrder(t68)
