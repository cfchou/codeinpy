__author__ = 'cfchou'

# https://leetcode.com/problems/maximum-gap/

'''
Given an unsorted array, find the maximum difference between the successive
elements in its sorted form.

Try to solve it in linear time/space.
Return 0 if the array contains less than 2 elements.
You may assume all elements in the array are non-negative integers and fit in
the 32-bit signed integer range.
'''

import math
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        ln = len(num)
        if ln < 2:
            return 0
        lo = hi = num[0]
        for i in range(1, ln):
            lo = min(lo, num[i])
            hi = max(hi, num[i])
        R = hi - lo + 1
        bucket_n = ln
        bucket_sz = 1
        if R <= ln:
            bucket_n = R
            # or resort to normal bucket sort
        else:
            bucket_sz = R / ln
            bucket_n = int(math.ceil(float(R) / bucket_sz))
        # bucket_n == R or bucket_n >= ln
        # print("%d, %d" % (bucket_n, bucket_sz))
        MI = -1         # lower bound of min
        MA = 2**32      # upper bound of max
        # [(max, min)]
        bucket_mm = [[MI, MA] for i in range(0, bucket_n)]

        for n in num:
            x = n - lo + 1
            i = int(math.ceil(float(x) / bucket_sz)) - 1
            bucket_mm[i][0] = max(bucket_mm[i][0], n)
            bucket_mm[i][1] = min(bucket_mm[i][1], n)

        assert(MI != bucket_mm[0][0] and MA != bucket_mm[0][1])
        assert(MI != bucket_mm[bucket_n - 1][0] and
               MA != bucket_mm[bucket_n - 1][1])
        # print(bucket_mm)
        max_gap = 0
        last_max = bucket_mm[0][0]
        for i in range(1, bucket_n):
            if MA == bucket_mm[i][1]:
                assert(MI == bucket_mm[i][0])
                continue
            if MI != last_max:
                max_gap = max(max_gap, bucket_mm[i][1] - last_max)
            last_max = bucket_mm[i][0]
        return max_gap



sol = Solution()
A = [0, 9, 1, 2, 8, 4, 7, 3]
A = [0, 9, 1, 2, 8, 1, 4, 7, 1, 3]
A = [2, 1, 0]
A = [1, 0]
A = [1, 1, 1]
A = [0, 0]
A = [2, 2, 0]
A = [1, 10]
print(sol.maximumGap(A))

