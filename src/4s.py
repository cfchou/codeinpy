__author__ = 'cfchou'

# https://oj.leetcode.com/problems/4sum/


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if None == num or 4 > len(num):
            return []
        sortedNum = sorted(num)
        sdict = self.twoSumDict(sortedNum)
        qs = set()
        for v1 in sorted(sdict.keys()):
            v2 = target - v1
            if v1 > v2:
                break
            s1 = sdict.get(v1, [])
            s2 = sdict.get(v2, [])
            # set only stores hashable so convert list to tuple
            lst = [tuple(sorted(t1 + t2)) for t1 in s1 for t2 in s2
                   if t1[0] not in t2 and t1[1] not in t2]
            for t in lst:
                qs.add(tuple(map(lambda i: sortedNum[i], t)))
        # set of tuples to list of lists
        ret = map(lambda t: list(t), qs)
        return ret

    def twoSumDict(self, num):
        # { v1: [ (i1, j2), (i3, i4), ...], ... }
        ret = {}
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                v = num[i] + num[j]
                s = ret.get(v, [])
                # append() changes the list inplace and returns None.
                s.append((i, j))
                ret[v] = s
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
            if num[i] > target:
                continue
            v = target - num[i]
            jj = tdict.get(v, [])
            ret += map(lambda j: (j, i), jj)
            # append() changes the list inplace and returns None.
            if tdict.get(num[i]):
                tdict[num[i]].append(i)
            else:
                tdict[num[i]] = [i]
        return ret

    def testTwoSum(self, num, target):
        sortedNum = sorted(num)
        shift = sortedNum[0]
        normalizedNum = map(lambda x: x - shift, sortedNum)
        normalizedTarget = target - 2 * shift
        ij = self.twoSum(normalizedNum, normalizedTarget)
        return map(lambda x: (sortedNum[x[0]], sortedNum[x[1]]), ij)


# num = [1, 0, -1, 0, -2, 2]
# target = 0
sol = Solution()
#print(sol.testTwoSum(num, target))
#print(sol.fourSum(num, target))

# num = [-500, -481, -480, -469, -437, -423, -408, -403, -397, -381, -379, -377, -353, -347, -337, -327, -313, -307, -299,
#       -278, -265, -258, -235, -227, -225, -193, -192, -177, -176, -173, -170, -164, -162, -157, -147, -118, -115, -83,
#       -64, -46, -36, -35, -11, 0, 0, 33, 40, 51, 54, 74, 93, 101, 104, 105, 112, 112, 116, 129, 133, 146, 152, 157,
#       158, 166, 177, 183, 186, 220, 263, 273, 320, 328, 332, 356, 357, 363, 372, 397, 399, 420, 422, 429, 433, 451,
#       464, 484, 485, 498, 499]
# target = 2139
# num = [-3,-2,-1,0,0,1,2,3]
# target = 0
#num = [1,-2,-5,-4,-3,3,3,5]
#target = -11
#num = [0]
#target = 0
num = [91277418, 66271374, 38763793, 4092006, 11415077, 60468277, 1122637, 72398035, -62267800, 22082642, 60359529,
       -16540633, 92671879, -64462734, -55855043, -40899846, 88007957, -57387813, -49552230, -96789394, 18318594,
       -3246760, -44346548, -21370279, 42493875, 25185969, 83216261, -70078020, -53687927, -76072023, -65863359,
       -61708176, -29175835, 85675811, -80575807, -92211746, 44755622, -23368379, 23619674, -749263, -40707953,
       -68966953, 72694581, -52328726, -78618474, 40958224, -2921736, -55902268, -74278762, 63342010, 29076029,
       58781716, 56045007, -67966567, -79405127, -45778231, -47167435, 1586413, -58822903, -51277270, 87348634,
       -86955956, -47418266, 74884315, -36952674, -29067969, -98812826, -44893101, -22516153, -34522513, 34091871,
       -79583480, 47562301, 6154068, 87601405, -48859327, -2183204, 17736781, 31189878, -23814871, -35880166, 39204002,
       93248899, -42067196, -49473145, -75235452, -61923200, 64824322, -88505198, 20903451, -80926102, 56089387,
       -58094433, 37743524, -71480010, -14975982, 19473982, 47085913, -90793462, -33520678, 70775566, -76347995,
       -16091435, 94700640, 17183454, 85735982, 90399615, -86251609, -68167910, -95327478, 90586275, -99524469,
       16999817, 27815883, -88279865, 53092631, 75125438, 44270568, -23129316, -846252, -59608044, 90938699, 80923976,
       3534451, 6218186, 41256179, -9165388, -11897463, 92423776, -38991231, -6082654, 92275443, 74040861, 77457712,
       -80549965, -42515693, 69918944, -95198414, 15677446, -52451179, -50111167, -23732840, 39520751, -90474508,
       -27860023, 65164540, 26582346, -20183515, 99018741, -2826130, -28461563, -24759460, -83828963, -1739800,
       71207113, 26434787, 52931083, -33111208, 38314304, -29429107, -5567826, -5149750, 9582750, 85289753, 75490866,
       -93202942, -85974081, 7365682, -42953023, 21825824, 68329208, -87994788, 3460985, 18744871, -49724457, -12982362,
       -47800372, 39958829, -95981751, -71017359, -18397211, 27941418, -34699076, 74174334, 96928957, 44328607,
       49293516, -39034828, 5945763, -47046163, 10986423, 63478877, 30677010, -21202664, -86235407, 3164123, 8956697,
       -9003909, -18929014, -73824245]
target = -236727523
print(sol.fourSum(num, target))
