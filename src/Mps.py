__author__ = 'cfchou'
import sys

# https://oj.leetcode.com/problems/maximum-product-subarray/

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        cMax = A[0]
        pMin = A[0]
        pMax = A[0]
        for e in A[1:]:
            a = e * pMin
            b = e * pMax
            pMin = min([e, a, b])
            pMax = max([e, a, b])
            cMax = max(cMax, pMax)
        return cMax

    def maxProductTry(self, A):
        mx = []
        for i in range(len(A)):
            # for j in range(len(A) - i):
            for j in range(len(A)):
                if 0 == i:
                    mx.append([A[j]])
                else:
                    if j + i <= len(A) - 1:
                        v = mx[j][0] * mx[j + 1][i - 1]
                        mx[j].append(v)
        return max(map(lambda a: max(a), mx))

sol = Solution()
arr = [2, -3, -1, -2, 4]
print(sol.maxProduct(arr))

