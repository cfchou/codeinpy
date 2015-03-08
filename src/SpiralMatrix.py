__author__ = 'cfchou'

# https://oj.leetcode.com/problems/spiral-matrix/

'''
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m < 1 or len(matrix[0]) < 1:
            return []
        n = len(matrix[0])
        ret = []
        self.round(0, 0, n, m, matrix, ret)
        return ret

    def round(self, x, y, a, b, mx, ret):
        #print(x, y, a, b)
        if 0 == a and 0 == b:
            return
        if 1 == a:
            for i in range(y, y + b):
                ret.append(mx[i][x])
            return
        elif 1 == b:
            for i in range(x, x + a):
                ret.append(mx[y][i])
            return

        xi = x + a - 1
        yi = y + b - 1

        for i in range(x, xi):
            ret.append(mx[y][i])
        for i in range(y, yi):
            ret.append(mx[i][xi])
        for i in range(xi, x, -1):
            ret.append(mx[yi][i])
        for i in range(yi, y, -1):
            ret.append(mx[i][x])
        if 2 >= a or 2 >= b:
            return
        self.round(x + 1, y + 1, max(0, a - 2), max(0, b - 2), mx, ret)

sol = Solution()
m1 = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
print(sol.spiralOrder(m1))
m2 = [ [ 1, 2, 3, 4 ], [ 4, 5, 6, 7 ], [ 7, 8, 9, 10 ] ]
print(sol.spiralOrder(m2))

m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(sol.spiralOrder(m3))

print(sol.spiralOrder([]))
print(sol.spiralOrder([[]]))
print(sol.spiralOrder([[1, 2, 3, 4]]))


# 3 * 5
m4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print(sol.spiralOrder(m4))

# 5 * 4
m5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
print(sol.spiralOrder(m5))

# 5 * 3
m6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
print(sol.spiralOrder(m6))

# 4 * 5
m7 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
print(sol.spiralOrder(m7))

# 2 * 10
m8 = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
print(sol.spiralOrder(m8))
