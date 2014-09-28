__author__ = 'cfchou'

# https://oj.leetcode.com/problems/divide-two-integers/

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        isPos = True
        if dividend < 0 < divisor or dividend > 0 > divisor:
            isPos = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        tbl = [0, divisor]  # 0, div, 2*div, 4*div, ...
        qtbl = [0, 1]  # 0, 1, 2, 4, ....
        end = 1
        residual = 0
        while True:
            endV = tbl[end]
            tbl.append(endV + endV)
            qtbl.append(qtbl[end] + qtbl[end])
            if endV > dividend:
                end -= 1
                residual = dividend - tbl[end]
                break
            else:
                end += 1
        # tbl = [0, div, 2*div, ...]; tbl[len(tbl) - 1] > dividend
        q = qtbl[end]
        q2, r = self.divideWithTbl(residual, tbl, qtbl)
        if isPos:
            return q + q2
        else:
            return - (q + q2)

    def divideWithTbl(self, dividend, tbl, qtbl):
        # tbl = [0, div, 2 * div, ... ]
        if tbl[1] == dividend:
            return 1, 0
        elif tbl[1] > dividend:
            return 0, dividend
        end = 2
        residual = 0
        while True:
            endV = tbl[end]
            if endV > dividend:
                end -= 1
                residual = dividend - tbl[end]
                break
            else:
                end += 1
        #q = self.indexToQuotient(end)
        q = qtbl[end]
        q2, r = self.divideWithTbl(residual, tbl, qtbl)
        return q + q2, r

    def divide2(self, dividend, divisor):
        # integer division in python 2.7 returns floor value. E.g.
        # -3/2 == -2

        isPos = True
        if dividend < 0 < divisor or dividend > 0 > divisor:
            isPos = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        tbl = [0, divisor]  # 0, div, 2*div, 4*div, ...
        qtbl = [0, 1]  # 0, 1, 2, 4, ....
        end = 1
        residual = 0
        while True:
            endV = tbl[end]
            tbl.append(endV + endV)
            qtbl.append(qtbl[end] + qtbl[end])
            if endV > dividend:
                end -= 1
                residual = dividend - tbl[end]
                break
            else:
                end += 1
        # tbl = [0, div, 2*div, ...]; tbl[len(tbl) - 1] > dividend
        q = qtbl[end]
        q2, r = self.divideWithTbl(residual, tbl, qtbl)
        if 0 != r:
            if isPos:
                return q + q2
            else:
                return - (q + q2) - 1
        else:
            if isPos:
                return q + q2
            else:
                return - (q + q2)
    def indexToQuotient(self, idx):
        if 0 == idx:
            return 1
        else:
            # reduce() needs a non-empty sequence
            return reduce(lambda acc, i: acc + acc, list(range(1, idx + 1)))



sol = Solution()
print(sol.divide(9, 2))
print(sol.divide(2, 9))
print(sol.divide(-9, 2))
print(sol.divide(9, -2))
print(sol.divide(2, -9))
print(sol.divide(-2, 9))
print(sol.divide(-2, -9))
print(sol.divide(0, 9))
print(sol.divide(0, -9))

