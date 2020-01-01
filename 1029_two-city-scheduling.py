# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/two-city-scheduling/

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs)/2
        if N == 0:
            return result
        tmp = []
        for i in range(len(costs)):
            a = costs[i][0]-costs[i][1]
            tmp.append([a, i])

        tmp.sort(key=lambda x: [x[0]])
        print tmp
        result = 0
        for i in range(N):
            index_A = tmp[i][1]
            result += costs[index_A][0]
            index_B = tmp[2*N-i-1][1]
            result += costs[index_B][1]

        return result

if __name__ == "__main__":
    s = Solution()
    print s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
