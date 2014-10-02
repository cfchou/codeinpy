__author__ = 'chifeng'

# https://oj.leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
import random
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        hl = self.listNodeToList(head)
        self.shuffle(hl)
        self.insertionSort(hl)
        ret = self.listToListNode(hl)
        return ret

    def listNodeToList(self, head):
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        return ret

    def listToListNode(self, lst):
        if 0 == len(lst):
            return None
        tmp = map(ListNode, lst)
        ret = tmp[len(tmp) - 1]
        for i in range(len(tmp) - 2, -1, -1):
            tmp[i].next = ret
            ret = tmp[i]
        return ret

    def shuffle(self, lst):
        random.seed()
        # random.shuffle(lst)
        #
        end = len(lst) - 1
        for i in range(end):
            j = random.randint(i, end)
            if i != j:
                lst[i], lst[j] = lst[j], lst[i]
        return lst

    def insertionSort(self, lst):
        for i in range(1, len(lst)):
            for j in range(i, 0, -1):
                if lst[j] >= lst[j - 1]:
                    break
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
        return lst


    def insertionSortListTry2(self, head):
        def insertSorted(sortedList, node):
            if None == sortedList:
                node.next = None
                return node
            if node.val >= sortedList.val:
                node.next = sortedList
                return node
            else:
                sortedList.next = insertSorted(sortedList.next, node)
                return sortedList

        def reverseList(head):
            if None == head:
                return None
            reversedHead = head
            head = head.next
            reversedHead.next = None
            while head:
                nnext = head.next
                head.next = reversedHead
                reversedHead = head
                head = nnext
            return reversedHead

        sortedHead = None
        while head:
            nnext = head.next
            sortedHead = insertSorted(sortedHead, head)
            head = nnext
        return reverseList(sortedHead)

        # Receive "maximum recursion depth exceeded" error as recursion is not "pythonic"
        # and tail recursion is not supported.
        def reverseListRecur(head):
            if None == head:
                return None, None
            if None == head.next:
                return head, head
            tmp = head
            head, end = reverseListRecur(head.next)
            end.next = tmp
            tmp.next = None
            return head, tmp

    def insertionSortListTry(self, head):
        def insertSorted(sortedList, node):
            if None == sortedList:
                node.next = None
                return node
            if node.val <= sortedList.val:
                node.next = sortedList
                return node
            else:
                sortedList.next = insertSorted(sortedList.next, node)
                return sortedList

        sortedHead = None
        nnext = None
        while head:
            nnext = head.next
            sortedHead = insertSorted(sortedHead, head)
            head = nnext
        return sortedHead

def printNodes(head):
    while head:
        print(head.val)
        head = head.next

def createList(n):
    if n < 1:
        return None
    start = ListNode(0)
    prev = start
    for i in range(1, n):
        prev.next = ListNode(i)
        prev = prev.next
    return start

sol = Solution()

lst = createList(10)
printNodes(lst)
print("------")
ret = sol.insertionSortList(lst)
printNodes(ret)


# arr = map(lambda i: ListNode(i), range(10))
# # 0,9,2,8,3
# arr[0].next = arr[9]
# arr[9].next = arr[2]
# arr[2].next = arr[8]
# arr[8].next = arr[3]
# printNodes(arr[0])
# ret = sol.insertionSortList(arr[0])
# printNodes(ret)




