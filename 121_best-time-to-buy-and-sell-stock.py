# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
#暴力法超出内存或时间限制
"""
        N = len(prices)
        if N <= 1:
            return 0
        maxPro = 0
        for i in range(N-1):
            for j in range(i+1, N):
                tmp = prices[j] - prices[i]
                if tmp > maxPro:
                    maxPro = tmp
        return maxPro
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        maxPro = 0
        minPri = float("inf")
        pro = prices[:]
        pro[0] = 0
        for i in xrange(len(prices)):
            minPri = min(minPri, prices[i])
            maxPro = max(maxPro, prices[i]-minPri)
        return maxPro

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([7,1,5,3,6,4])
