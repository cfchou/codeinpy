__author__ = 'chifeng'

# https://oj.leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
import random
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class DListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class Solution:
    def __init__(self):
        self.asc = None
        self.dsc = None
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        self.asc, self.dsc = None, None
        def appendTo(node, cur):
            next = cur.next
            cur.next = node
            node.prev = cur
            node.next = next
            if None == node.next:
                self.dsc = node
            else:
                next.prev = node
            return
        def preppendTo(node, cur):
            prev = cur.prev
            cur.prev = node
            node.prev = prev
            node.next = cur
            if None == node.prev:
                self.asc = node
            else:
                prev.next = node
            return

        while head:
            node = DListNode(head.val)
            head = head.next
            if None == self.asc:
                self.asc = DListNode(node.val)
                self.dsc = self.asc
                continue
            ascCur, dscCur = self.asc, self.dsc
            while True:
                #assert None == self.asc.prev and None == self.dsc.next
                if self.asc is self.dsc:
                    if node.val <= self.asc.val:
                        self.asc = node
                    else:
                        self.dsc = node
                    self.asc.next = self.dsc
                    self.dsc.prev = self.asc
                    break

                #assert ascCur and dscCur
                if ascCur is dscCur:
                    if node.val <= ascCur.val:
                        preppendTo(node, ascCur)
                    else:
                        appendTo(node, ascCur)
                    break
                # cross
                if ascCur.prev is dscCur:
                    #assert dscCur.next is ascCur
                    if node.val <= dscCur.val:
                        preppendTo(node, dscCur)
                    elif node.val <= ascCur.val:
                        preppendTo(node, ascCur)
                    else:
                        appendTo(node, ascCur)
                    break

                if node.val <= ascCur.val:
                    preppendTo(node, ascCur)
                    break
                if node.val >= dscCur.val:
                    appendTo(node, dscCur)
                    break
                ascCur = ascCur.next
                dscCur = dscCur.prev
            # while True
        # while head

        ret = None
        end = None
        cur = self.asc
        while cur:
            if None == ret:
                ret = ListNode(cur.val)
                end = ret
                cur = cur.next
                continue
            end.next = ListNode(cur.val)
            end = end.next
            cur = cur.next
        return ret

    def printFw(self, head):
        line = ">>>\t\t"
        while head:
            line += ". {}".format(head.val)
            head = head.next
        print(line)

    def printBw(self, head):
        line = "<<<\t\t"
        while head:
            line += ". {}".format(head.val)
            head = head.prev
        print(line)




def printNodes(head):
    while head:
        print(head.val)
        head = head.next

def printNodesRow(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    print(lst)

def createList(lst):
    if len(lst) < 1:
        return None
    start = ListNode(lst[0])
    prev = start
    for i in lst[1:]:
        prev.next = ListNode(i)
        prev = prev.next
    return start

def createRandomList(sz, seq):
    lst = map(lambda x: random.choice(seq), range(sz))
    return createList(lst)


def test1():
    sol = Solution()
    lst = createList(range(5000))
    #printNodes(lst)
    print("------")
    ret = sol.insertionSortList(lst)
    return ret

def test2():
    sol = Solution()
    lst = createList(range(5000, -1, -1))
    #printNodes(lst)
    print("------")
    ret = sol.insertionSortList(lst)
    return ret

def test3():
    sol = Solution()
    lst = createRandomList(5000, range(-1000, 1001))
    printNodesRow(lst)
    print("------")
    ret = sol.insertionSortList(lst)
    return ret

def test4():
    sol = Solution()
    lst = createRandomList(10, range(-10, 10))
    printNodes(lst)
    print("------")
    ret = sol.insertionSortList(lst)
    return ret

def test5():
    sol = Solution()
    arr = [7, 5, -5, -3, -7, 8]
    lst = createList(arr)
    printNodes(lst)
    print("------")
    ret = sol.insertionSortList(lst)
    return ret

test3()
#printNodes(test5())


class Solution2:
    def insertionSortList(self, head):
        sortedLN = head
        if None == head:
            return None
        head = head.next
        sortedLN.next = None
        while head:
            # dettach first node from head
            node = head
            head = head.next
            node.next = None

            if node.val <= sortedLN.val:
                node.next = sortedLN
                sortedLN = node
                continue
            snode = sortedLN
            while True:
                assert node.val > snode.val
                if None == snode.next:
                    snode.next = node
                    break
                else:
                    if node.val <= snode.next.val:
                        tmp = snode.next
                        snode.next = node
                        node.next = tmp
                        break
                    else:
                        snode = snode.next
        return sortedLN

    def insertionSortListTry3(self, head):
        hl = self.listNodeToList(head)
        #self.shuffle(hl)
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

    def insertionSort(self, lst):
        for i in range(1, len(lst)):
            for j in range(i, 0, -1):
                if lst[j] >= lst[j - 1]:
                    break
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
        return lst

    def shuffle(self, lst):
        random.seed()
        # random.shuffle(lst)
        end = len(lst) - 1
        for i in range(end):
            j = random.randint(i, end)
            if i != j:
                lst[i], lst[j] = lst[j], lst[i]
        return lst
