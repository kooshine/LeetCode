# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        tmp = n
        i = 1
        while tmp != 0:
            count += (n/(i*10)) * i
            num = n % (i * 10)
            if num >= 2 * i:
                count += i
            elif num >= i and num < 2*i:
                count += (num-i+1)

            tmp = n/(i*10)
            i = i * 10
        return count

if __name__ == "__main__":
    s = Solution()
    print s.NumberOf1Between1AndN_Solution(1234)
