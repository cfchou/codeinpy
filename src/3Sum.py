__author__ = 'cfchou'

# https://leetcode.com/problems/3sum/
'''
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},
A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        ns, dict = self.sort_and_map(num)
        # print("ns: %s" % ns)
        # print("dict: %s" % dict)
        ln = len(ns)
        if ns[0] * ns[ln - 1] > 0:
            return []
        tbl = [[0 for b in range(0, ln)] for c in range(0, ln)]
        for i, c in enumerate(ns):
            for j, b in enumerate(ns):
                if b <= c:
                    tbl[i][j] = -c - b

        # print(tbl)
        ret = []
        for i in range(ln - 1, -1, -1):
            for j in range(0, ln):
                if ns[j] > ns[i]:
                    break
                a = tbl[i][j]
                if ns[0] <= a <= ns[j] and a in dict:
                    if a == ns[i] == ns[j]:
                        if dict[a] > 2:
                            ret.append([a, a, a])
                            # print("1... %d, %d, %d" % (a, a, a))
                    elif ns[j] == ns[i]:
                        if dict[ns[j]] > 1:
                            ret.append([a, ns[j], ns[i]])
                            # print("2... %d, %d, %d" % (a, ns[j], ns[i]))
                    elif a == ns[j]:
                        if dict[ns[j]] > 1:
                            ret.append([a, a, ns[i]])
                            # print("3... %d, %d, %d" % (a, a, ns[i]))
                    else:
                        ret.append([a, ns[j], ns[i]])
                        # print("4... %d, %d, %d" % (a, ns[j], ns[i]))
        return ret

    def sort_and_map(self, num):
        sn = sorted(num)
        cs = []
        dict = {}
        for n in sn:
            t = dict.get(n)
            if None == t:
                cs.append(n)
                dict[n] = 1
            else:
                dict[n] = t + 1
        return cs, dict
    '''
    def threeSum(self, num):
        if len(num) < 3:
            return []
        bs, cs, dict = self.sort_and_map(num)
        print("bs: %s" % bs)
        print("cs: %s" % cs)
        lb = len(bs)
        lc = len(cs)
        if cs[0] * cs[lc - 1] > 0:
            return []
        tbl = [[0 for b in range(0, lb)] for c in range(0, lc)]
        for i, c in enumerate(cs):
            for j, b in enumerate(bs):
                if b <= c:
                    tbl[i][j] = -c - b

        print(tbl)
        ret = []
        for i in range(lc - 1, -1, -1):
            for j in range(0, lb):
                if j == lb - 1 or bs[j + 1] > cs[i]:
                    break
                a = tbl[i][j]
                if bs[0] <= a <= bs[j]:
                    if j > 0 and a == bs[j] == bs[j - 1]:
                        ret.append([a, bs[j], cs[i]])
                        print("... %d, %d, %d" % (a, bs[j], cs[i]))
                    elif a != bs[j] and a in dict:
                        ret.append([a, bs[j], cs[i]])
                        print("--- %d, %d, %d" % (a, bs[j], cs[i]))
        return ret

    def sort_and_map(self, num):
        sn = sorted(num)
        bs = []
        cs = []
        dict = {}
        for n in sn:
            t = dict.get(n)
            if None == t:
                bs.append(n)
                cs.append(n)
                dict[n] = 1
            elif 1 == t or 2 == t:
                bs.append(n)
                dict[n] = t + 1
            else:
                dict[n] = t + 1
        return bs, cs, dict
    '''

    # Or we can shift num to be all positives
    # a + b + c = 3 * -min
    # def threeSum2(self, num):


sol = Solution()
num = [0, 0, 0]
print(sol.threeSum(num))
num = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(num))
num = [11, 10, -2, -13, 5, -2, 8, 12, -9, 11]
print(sol.threeSum(num))

'''
import random
num = [random.randrange(-15, 15) for i in range(0, 10)]
print(num)
print(sol.threeSum(num))
'''


