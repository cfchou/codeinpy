# https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if None == root:
            return []
        cont = [root]
        values = []
        level = 1
        while len(cont) > 0:
            children = list()
            children_vals = list()
            for i in range(len(cont) - 1, -1, -1):
                t = cont[i]
                children_vals.append(t.val)
                if 1 == level % 2:
                    if None != t.left:
                        children.append(t.left)
                    if None != t.right:
                        children.append(t.right)
                else:
                    if None != t.right:
                        children.append(t.right)
                    if None != t.left:
                        children.append(t.left)
            cont = children
            #print("children: %s" % children)
            values.append(children_vals)
            #print("children_vals: %s" % children_vals)
            level += 1
        return values


sol = Solution()

print(sol.zigzagLevelOrder(None))

ns = [TreeNode(i) for i in range(0, 10)]
ns[1].left = ns[2]
ns[1].right = ns[3]
ns[2].left = ns[4]
ns[2].right = ns[5]
ns[3].left = ns[6]
ns[3].right = ns[7]
print(sol.zigzagLevelOrder(ns[1]))


ns = [TreeNode(i) for i in range(0, 21)]
ns[3].left = ns[9]
ns[3].right = ns[20]
ns[20].left = ns[15]
ns[20].right = ns[7]
print(sol.zigzagLevelOrder(ns[3]))
