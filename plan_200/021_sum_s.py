# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        m = len(array)
        start = 0
        end = m - 1
        while start < end:
            total = array[start] + array[end]
            if total > tsum:
                end -= 1
            elif total < tsum:
                start += 1
            else:
                return array[start], array[end]
        return []
        """
        m = len(array)
        for i in range(m):
            if array[i] < tsum/2:
                for j in range(i+1, m):
                    if array[j] == tsum - array[i]:
                        return array[i], array[j]
        return []
        """

