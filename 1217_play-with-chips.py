# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/play-with-chips/

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        odd = 0
        even = 0
        for item in chips:
            if item % 2:
                odd += 1
            else:
                even += 1
        return even if odd > even else odd

