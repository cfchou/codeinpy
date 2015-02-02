__author__ = 'cfchou'

# https://oj.leetcode.com/problems/climbing-stairs/

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        # cs[i] = cs[i - 1] + cs[i - 2]
        cs = [0, 1, 2]
        for i in range(3, n + 1):
            cs.append(cs[i - 1] + cs[i - 2])
        return cs[n]

sol = Solution()
ans = sol.climbStairs(5)
print "%d" % (ans)