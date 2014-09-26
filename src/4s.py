__author__ = 'cfchou'


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
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
        ret = []
        for t in range(0, normalizedTarget + 1):
            if t > normalizedTarget - t:
                break
            ns1 = tdict.get(t)
            ns2 = tdict.get(normalizedTarget - t)
            if ns1 and ns2:
                ret += [sorted(a + b) for a in ns1 for b in ns2
                        if a[0] not in b and a[1] not in b]
        return ret

    def twoSum(self, num, target):
        """
        :param num: Sorted positive integers.
        :param target: Positive integer.
        :return: List of tuples.
        """
        ret = []
        tdict = {}
        for i in range(0, len(num)):
            v = target - num[i]
            j = tdict.get(v)
            if j:
                # FIX:
                # All pairs should be considered. e.g.
                # [2, 2, 2], target = 4
                # there should be 3 pairs.
                del tdict[v]
                ret += (j, i)
            else:
                tdict[num[i]] = i

        return ret
