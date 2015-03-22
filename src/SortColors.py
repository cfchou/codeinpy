__author__ = 'cfchou'

# https://leetcode.com/problems/sort-colors/

'''
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red, white
and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem
'''

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        la = len(A)
        p, q = 0, la - 1
        while True:
            while p < q:
                if p < la and 0 == A[p]:
                    p += 1
                if q >= 0 and 2 == A[q]:
                    q -= 1
                if 0 != A[p] and 2 != A[q]:
                    break
            if p >= q:
                return
            s = p
            while s <= q:
                if 0 == A[s]:
                    self.swap(p, s, A)
                    break
                elif 2 == A[s]:
                    self.swap(s, q, A)
                    break
                else:
                    s += 1
            if s >= q:
                return

    def swap(self, i, j, A):
        assert(0 <= i < len(A) and 0 <= j <= len(A))
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp


sol = Solution()

import random
A = [random.randrange(0, 3) for i in range(1, 10)]
A = [0, 0, 2, 0, 1, 2, 1, 2, 0]
A = []
A = [0]
A = [1,0]
A = [1,2,0]
A = [2,1,0]
A = [1,0,2]
A = [0,0,2]
A = [1,0,0]
print(A)
sol.sortColors(A)
print(A)
