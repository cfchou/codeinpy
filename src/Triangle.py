__author__ = 'chifeng'

# https://leetcode.com/problems/triangle/
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n
is the total number of rows in the triangle.
'''
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        ln = len(triangle)
        if 0 == ln:
            return 0
        tbl = [i for i in triangle[ln - 1]]
        for i in range(ln - 2, -1, -1):
            tmp = []
            for j in range(0, i + 1):
                tmp.append(triangle[i][j] + min(tbl[j], tbl[j + 1]))
            tbl = tmp
        return tbl[0]

sol = Solution()
A = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
print(sol.minimumTotal(A))


