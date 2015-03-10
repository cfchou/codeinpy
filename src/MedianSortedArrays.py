__author__ = 'cfchou'

# https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

import math
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        assert(not([] == A and [] == B))
        lA = len(A)
        lB = len(B)
        nA, nB = 0, 0
        isOdd = (lA + lB) % 2 != 0
        k = int((lA + lB) / 2)
        if isOdd:
            k += 1

        if lA >= lB:
            nA, nB = self.find(A, B, 0, k, k)
        else:
            nB, nA = self.find(B, A, 0, k, k)
        #print("(%d, %d)" % (nA, nB))

        m1 = 0
        if 0 == nA:
            m1 = float(B[nB - 1])
        elif 0 == nB:
            m1 = float(A[nA - 1])
        else:
            m1 = float(max(A[nA - 1], B[nB - 1]))

        if isOdd:
            return m1
        else:
            if nA == lA:
                return float(m1 + B[nB]) / 2
            elif nB == lB:
                return float(m1 + A[nA]) / 2
            else:
                return float(m1 + min(A[nA], B[nB])) / 2

    # take n in [atLeast, atMost] from L1
    def find(self, L1, L2, atLeast, atMost, total):
        #print("[%d, %d]" % (atLeast, atMost))
        if atLeast == atMost:
            return atLeast, total - atLeast

        # middle >= atLeast
        middle = int((atLeast + atMost) / 2)
        fromL2 = min(total - middle, len(L2))  # fromL2 <= len(L2)
        fromL1 = total - fromL2
        #print("\t%d, %d, %d" % (fromL1, fromL2, middle))

        if fromL1 < atMost and L1[fromL1] < L2[fromL2 - 1]:
            return self.find(L1, L2, fromL1 + 1, atMost, total)
        elif fromL1 > atLeast and fromL2 < len(L2) and L1[fromL1 - 1] > L2[fromL2]:
            return self.find(L1, L2, atLeast, fromL1 - 1, total)
        else:
            return fromL1, fromL2

sol = Solution()
A = [1, 2, 3, 4, 11, 13, 15]
B = [2, 4, 5, 6, 12]
#print(sol.find(A, B, 0, 6, 6))
#A = [1, 2, 3, 4, 11, 13, 15]
#B = []
#print(sol.find(A, B, 0, 4, 4))

#A = [1]
#B = [1]
#print(sol.find(A, B, 0, 1, 1))

#A = [3, 4, 11, 13, 15, 18, 20]
#B = [3, 5, 7]
#print(sol.find(A, B, 0, 5, 5))



# A = [100000]
# B = [100001]
print(sol.findMedianSortedArrays(A, B))




