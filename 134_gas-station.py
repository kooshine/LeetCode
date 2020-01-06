# -*- coding: utf-8 -*-
import time

#https://leetcode-cn.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(gas)

        for i in range(N):
            if gas[i] < cost[i]:
                continue
            s = 0
            c = 0
            j = i
            while c < N:
                s += gas[j]-cost[j]
                if s < 0:
                    break
                j = (j+1)%N
                c += 1

            if c == N:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
    print s.canCompleteCircuit([2,3,4], [3,4,3])
    print s.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])
    print s.canCompleteCircuit([3,1,1], [1,2,2])
