__author__ = 'cfchou'

# https://oj.leetcode.com/problems/dungeon-game/

class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        print("m,n = %d, %d" % (m, n))
        if m * n == 1:
            return 1 + max(0, -dungeon[0][0])
        hs = [[0] * n] * m
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                self.karma_update(i, j, hs, dungeon)
                #print("[%d][%d]: %d" % (i, j, hs[i][j]))
        return 1 + hs[0][0]

    def karma_update(self, i, j, hs, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        d = dungeon[i][j]

        if n - 1 == j and m - 1 == i:
            hs[i][j] = max(0, -d)
            return
        if n - 1 == j:  # rightmost
            hs[i][j] = self.karma(d, hs[i + 1][j])
            return
        if m - 1 == i:  # bottom
            hs[i][j] = self.karma(d, hs[i][j + 1])
            return
        a1 = self.karma(d, hs[i + 1][j])
        a2 = self.karma(d, hs[i][j + 1])
        hs[i][j] = min(a1, a2)

    def karma(self, d, least_karma):
        if d < 0:
            return least_karma - d
        else:
            return max(0, least_karma - d)

sol = Solution()
t1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(sol.calculateMinimumHP(t1))
