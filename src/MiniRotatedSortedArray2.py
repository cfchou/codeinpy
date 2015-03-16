__author__ = 'cfchou'

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicates.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        assert (len(num) > 0)
        n = self.findMinAt(0, len(num) - 1, num)
        return num[n]

    def findMinAt(self, lo, hi, L):
        if lo == hi:
            return lo
        mi = int((lo + hi) / 2)
        n1 = self.findMinAt(lo, mi, L)
        if mi < hi:
            n2 = self.findMinAt(mi + 1, hi, L)
            if L[n1] < L[n2]:
                return n1
            else:
                return n2
        return n1


import random

def testFindMin():
    sol = Solution()
    k = random.randrange(1, 20)
    rr = [random.randrange(-20, 20) for i in range(0, k)]
    arr = sorted(rr)
    p = random.randrange(0, 10)
    brr = arr[p:] + arr[0:p]
    m = sol.findMin(brr)
    print(brr)
    print("%d ?= %d" % (arr[0], m))
    assert(arr[0] == m)

for i in range(0, 100):
    testFindMin()



