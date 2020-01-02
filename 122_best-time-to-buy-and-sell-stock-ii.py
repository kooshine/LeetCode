# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/


class Solution(object):
      def maxProfit(self, prices):
          """
                  :type prices: List[int]
          :rtype: int
                  """
          N = len(prices)
          if N <= 1:
              return 0

          result = 0
          for i in range(N-1):
              tmp = prices[i+1]- prices[i]
              if tmp > 0:
                  result += tmp
          return result

