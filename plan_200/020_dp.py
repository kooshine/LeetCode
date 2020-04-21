# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [item for item in array]

        for i in range(1,len(array)):
            dp[i] = self.get_max(dp[i-1]+array[i], array[i])
        return max(dp)

    def get_max(self,a, b):
        return a if a > b else b
