# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        bitmask = 0
        for item in array:
            bitmask ^= item
        diff = bitmask & (-bitmask)
        nums = 0
        for item in array:
            if item & diff:
                nums ^= item
        return [nums, bitmask ^ nums]
