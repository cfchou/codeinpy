__author__ = 'chifeng'

# https://oj.leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        ws = []
        for s in s.strip().split():
            ss = s.strip()
            if ss:
                ws.append(ss)
        s = ""
        i = len(ws)
        if i > 0:
            i -= 1
            s = ws[i]
            while i > 0:
                i -= 1
                s += (" " + ws[i])
        return s


sol = Solution()
print(sol.reverseWords(" 111 xxx 333    "))
