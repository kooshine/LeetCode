# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.result = []
    def Permutation(self, ss):
        # write code here
        m = len(ss)
        if m <= 1:
            return [ss]
        tmp = ""
        self.dfs(ss, tmp)
        return self.result

    def dfs(self, s, tmp):
        m = len(s)
        if m <= 0:
            self.result.append(tmp)
            return
        repeat = set()
        for i in range(m):
            if s[i] in repeat: #剪枝
                continue
            repeat.add(s[i])
            tmp += s[i]
            self.dfs(s[:i]+s[i+1:], tmp)
            tmp = tmp[:-1]

if __name__ == "__main__":
    s = Solution()
    print s.Permutation("abb")

