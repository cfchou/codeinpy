__author__ = 'chifeng'

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#Find the minimum element.
#You may assume no duplicate exists in the array.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        assert(len(num) != 0)
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
            else:  # no duplicate exists
                return n2
        else:
            return n1

sol = Solution()
print(sol.findMin([0]))
print(sol.findMin([0, 1]))
print(sol.findMin([1, 0]))
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
print(sol.findMin([14, 15, 16, 17, 0, 1, 2, 3, 4, 5]))


