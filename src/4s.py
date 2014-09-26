__author__ = 'cfchou'

# https://oj.leetcode.com/problems/4sum/


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if None == num or 0 == len(num):
            return []
        sortedNum = sorted(num)
        shift = sortedNum[0]
        normalizedNum = map(lambda x: x - shift, sortedNum)
        normalizedTarget = target - 4 * shift

        # { t1: [ (n1, n2), (n3, n4), ...],
        #   t2: [ (n1, n3), (n2, n4), ...], ... }
        tdict = {}
        for t in range(0, normalizedTarget + 1):
            ns = self.twoSum(normalizedNum, t)
            if len(ns) > 0:
                tdict[t] = ns
        qs = set()
        for t in range(0, normalizedTarget + 1):
            if t > normalizedTarget - t:
                break
            ns1 = tdict.get(t)
            ns2 = tdict.get(normalizedTarget - t)
            if ns1 and ns2:
                lst = [tuple(sorted(a + b)) for a in ns1 for b in ns2
                       if a[0] not in b and a[1] not in b]
                map(lambda l: qs.add(l), lst)
        ret = []
        for q in qs:
            ret.append(map(lambda i: sortedNum[i], q))
        return ret

    def twoSum(self, num, target):
        """
        O(n^2) for the WORST case, e.g. { num: [2, 2, 2, 2], target: 4 }
        :param num: Sorted positive integers.
        :param target: Positive integer.
        :return: List of tuples.
        """
        ret = []
        # { v1: [n1, n4, n5], v2: [ n2, n3], ... }
        tdict = {}
        for i in range(0, len(num)):
            v = target - num[i]
            jj = tdict.get(v, [])
            ret += map(lambda j: (j, i), jj)
            # append() changes the list inplace and returns None.
            if tdict.get(num[i]):
                tdict[num[i]].append(i)
            else:
                tdict[num[i]] = [i]
            '''
            if j:
                # FIX:
                # All pairs should be considered. e.g.
                # [2, 2, 2], target = 4
                # there should be 3 pairs.
                del tdict[v]
                ret += (j, i)
            else:
                tdict[num[i]] = i
            '''
        return ret

    def testTwoSum(self, num, target):
        sortedNum = sorted(num)
        shift = sortedNum[0]
        normalizedNum = map(lambda x: x - shift, sortedNum)
        normalizedTarget = target - 2 * shift
        ij = self.twoSum(normalizedNum, normalizedTarget)
        return map(lambda x: (sortedNum[x[0]], sortedNum[x[1]]), ij)



num = [1, 0, -1, 0, -2, 2]
target = 0
sol = Solution()
print(sol.testTwoSum(num, target))
print(sol.fourSum(num, target))

num = [-500,-481,-480,-469,-437,-423,-408,-403,-397,-381,-379,-377,-353,-347,-337,-327,-313,-307,-299,-278,-265,-258,-235,-227,-225,-193,-192,-177,-176,-173,-170,-164,-162,-157,-147,-118,-115,-83,-64,-46,-36,-35,-11,0,0,33,40,51,54,74,93,101,104,105,112,112,116,129,133,146,152,157,158,166,177,183,186,220,263,273,320,328,332,356,357,363,372,397,399,420,422,429,433,451,464,484,485,498,499]
target = 2139
print(sol.fourSum(num, target))

