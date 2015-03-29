__author__ = 'cfchou'
# https://leetcode.com/problems/edit-distance/
'''
Given two words word1 and word2, find the minimum number of steps required to
convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

Edit Distance is also called Levenshtein Distance.
'''
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if 0 == len(word1):
            return len(word2)
        if 0 == len(word2):
            return len(word1)
        # assert(len(word1) > 0 and len(word2) > 0)

        tbl = [[0 for j in range(0, len(word2))] for i in range(0, len(word1))]
        if word1[0] == word2[0]:
            tbl[0][0] = 0
        else:
            tbl[0][0] = 1

        for i in range(1, len(word1)):
            if word1[i] == word2[0]:
                tbl[i][0] = i
            else:
                tbl[i][0] = 1 + min(i, tbl[i - 1][0])

        for j in range(1, len(word2)):
            if word1[0] == word2[j]:
                tbl[0][j] = j
            else:
                tbl[0][j] = 1 + min(j, tbl[0][j - 1])
        # print(tbl)
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    tbl[i][j] = tbl[i - 1][j - 1]
                else:
                    tbl[i][j] = 1 + min(tbl[i - 1][j - 1], tbl[i - 1][j],
                                        tbl[i][j - 1])
        # print("========================")
        # print(tbl)
        return tbl[len(word1) - 1][len(word2) - 1]


sol = Solution()

# print(sol.minDistance("adabca", "acb"))
print(sol.minDistance("acb", "adabca"))
print(sol.minDistance("bca", "acbada"))
print(sol.minDistance("acb", "bca"))
print(sol.minDistance("acacb", "bbaca"))




