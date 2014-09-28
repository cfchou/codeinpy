__author__ = 'chifeng'

# https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Given a singly linked list where elements are sorted in ascending
# order, convert it to a height balanced BST

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None:
            return None
        lst = [head.val]
        node = head.next
        while None != node:
            lst.append(node.val)
            node = node.next
        return self.build(lst)

    def build(self, arr):
        sz = len(arr)
        if 0 == sz:
            return None
        elif 1 == sz:
            return TreeNode(arr[0])
        else:
            mid = int((sz - 1) / 2)
            tr = TreeNode(arr[mid])
            tr.left = self.build(arr[:mid])
            tr.right = self.build(arr[mid + 1:])
            return tr


from functools import reduce
def genSortedListNodes(max):
    def add(l, x):
        l.next = ListNode(x)
        return l.next
    h = ListNode(0)
    reduce(add, range(1, max + 1), h)
    return h

def dfs(fun, tr):
    if None != tr:
        dfs(fun, tr.left)
        fun(tr.val)
        dfs(fun, tr.right)


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next = ListNode(3)

lst = genSortedListNodes(5)
tr = Solution().sortedListToBST(lst)

def p(s):
   print s

dfs(p, tr)


