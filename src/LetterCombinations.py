__author__ = 'cfchou'

# https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ret = ['']
        if 0 == len(digits):
            return ret
        ret = mapping[digits[0]]
        for d in digits[1:]:
            tmp = ret[:]
            ret = [t + m for m in mapping[d] for t in tmp]
        return ret


sol = Solution()
ans = sol.letterCombinations('')
print(ans)
ans = sol.letterCombinations('23')
print(ans)
