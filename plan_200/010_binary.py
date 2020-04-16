# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        """
        if n < 0:  #重点
            n = 2**32+n
        nums = 0
        while n > 0:
            if n % 2 == 1:
                nums += 1
            n = n / 2
        return nums
        """

        nums = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                nums += 1
            mask = mask << 1
        return nums

