# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        child = [i for i in range(n)]
        idx = 0
        while n > 1:
            idx = (idx + m - 1)% n
            child.pop(idx)
            n -= 1
        return child[0] if child else -1

if __name__ == "__main__":
    s = Solution()
    print s.LastRemaining_Solution(5, 3)
