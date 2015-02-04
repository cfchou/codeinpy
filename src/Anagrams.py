__author__ = 'cfchou'

# https://oj.leetcode.com/problems/anagrams/
# Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}
        ret = []
        for s in strs:
            ss = ''.join(sorted(s))
            v = dict.setdefault(ss, [])
            v.append(s)
        for d in dict.values():
            if len(d) > 1:
                ret[len(ret):] = d
        return ret

sol = Solution()
ans = sol.anagrams(["xbc", "jbo", "bcx"])
print(ans)