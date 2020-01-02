# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        while K > 0:
            min_val = min(A)
            A.remove(min_val)
            A.append(-min_val)
            K -= 1
        return sum(A)
