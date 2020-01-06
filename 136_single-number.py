# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
                count = dict()
        N = len(nums)
        if N <= 0:
            return
        for i in range(N):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        for k, v in count.items():
            if v == 1:
                return k
