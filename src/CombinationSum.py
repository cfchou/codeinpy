__author__ = 'chifeng'

# https://leetcode.com/problems/combination-sum/

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        sc = sorted(candidates)
        tbl = [[0 for j in range(0, len(sc))]
               for i in range(0, target + 1)]
        for i in range(0, target + 1):
            for j in range(0, len(sc)):
                tbl[i][j] = i - sc[j]

        # for i in range(0, target + 1):
        #     print(tbl[i])
        # print('--------------')
        ret = self.find_sum(sc, tbl, target, len(sc) - 1)
        return ret

    def find_sum(self, candidates, tbl, i, j):
        ret = []
        for jj in range(j, -1, -1):
            if 0 == tbl[i][jj]:
                ret.append([candidates[jj]])
            elif 0 < tbl[i][jj]:
                lists = self.find_sum(candidates, tbl, tbl[i][jj], jj)
                lists2 = [l + [candidates[jj]] for l in lists]
                ret += lists2
        return ret


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.combinationSum([2, 3, 5], 5))
