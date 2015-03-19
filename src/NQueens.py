__author__ = 'cfchou'

# https://leetcode.com/problems/n-queens/
'''
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        down = [[True for i in range(0, n)] for i in range(0, n)]
        downR = [[True for i in range(0, n)] for i in range(0, n)]
        downL = [[True for i in range(0, n)] for i in range(0, n)]
        return self.nextRow(n, 0, down, downL, downR)

    def nextRow(self, n, i, dn, dl, dr):
        # print("%d ---------" % i)
        ret = []
        if n < 1:
            return ret
        if i == n - 1:  # last row
            for j in range(0, n):
                if dn[i][j] and dl[i][j] and dr[i][j]:
                    tmp = ['.'] * n
                    tmp[j] = 'Q'
                    # string.join turns iterable to string.
                    # it is preferred to concatenation.
                    # concatenation takes a list.
                    ret.append(["".join(tmp)])
            return ret
        candidates = []
        for j in range(0, n):
            if not dn[i][j]:
                dn[i + 1][j] = False
            if (not dl[i][j]) and j > 0:
                dl[i + 1][j - 1] = False
            if (not dr[i][j]) and j < n - 1:
                dr[i + 1][j + 1] = False
            if dn[i][j] and dl[i][j] and dr[i][j]:
                candidates.append(j)
        # print(candidates)
        for j in candidates:
            tmp = ['.'] * n
            # print(" %d, %d" % (i, j))
            orig_dl, orig_dr = None, None
            orig_dn = dn[i + 1][j]
            dn[i + 1][j] = False
            if 0 < j:
                orig_dl = dl[i + 1][j - 1]
                dl[i + 1][j - 1] = False
            if j < n - 1:
                orig_dr = dr[i + 1][j + 1]
                dr[i + 1][j + 1] = False
            tmp[j] = 'Q'
            rs = self.nextRow(n, i + 1, dn, dl, dr)
            for m in rs:
                # concatenation takes a list
                m[:0] = ["".join(tmp)]
                ret.append(m)
            dn[i + 1][j] = orig_dn
            if 0 < j:
                dl[i + 1][j - 1] = orig_dl
            if j < n - 1:
                dr[i + 1][j + 1] = orig_dr

        for j in range(0, n):
            dn[i + 1][j] = True
            dl[i + 1][j] = True
            dr[i + 1][j] = True
        return ret
                    

sol = Solution()
ret = sol.solveNQueens(4)
print(ret)
print(len(ret))


print(sol.solveNQueens(1))
print(sol.solveNQueens(2))
print(sol.solveNQueens(3))
ret = sol.solveNQueens(8)
print(len(ret))



