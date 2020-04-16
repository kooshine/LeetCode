# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        #return self.Fibonacci(n-1) + self.Fibonacci(n-2)
        ret1, ret2 = 0,1
        for i in range(2, n+1):
            tmp = ret1 + ret2
            ret1 = ret2
            ret2 = tmp

        return ret2

if __name__ == "__main__":
    s = Solution()
    print s.Fibonacci(5)
