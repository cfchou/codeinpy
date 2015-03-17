__author__ = 'chifeng'

# https://leetcode.com/problems/repeated-dna-sequences/
'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T.
Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        if 10 > len(s):
            return []

        keeping = []
        ret = []
        dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        tbl = [0] * (4 ** 10)
        prev_idx = 0
        for i in range(0, 10):
            prev_idx += dict[s[i]] * (4 ** i)
        tbl[prev_idx] += 1

        for i in range(1, len(s) - 9):
            prev_idx = self.cal_next_index(dict, s, i, prev_idx)
            if 1 == tbl[prev_idx]:
                keeping.append(i)
            tbl[prev_idx] += 1
        for i in keeping:
            ret.append(s[i:i + 10])
        return ret

    def cal_next_index(self, dict, s, i, prev_idx):
        assert(i + 9 < len(s))
        c = 262144  # 4**9
        return dict[s[i + 9]] * c + int(prev_idx / 4)


sol = Solution()
#print(sol.findRepeatedDnaSequences("AAAAAAAAAC"))
s = []
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAA"
# s = "AAAAAAAAAAAA"
# ["AAAAAAAAAA","AAAAAAAAAA"]
print(sol.findRepeatedDnaSequences(s))


