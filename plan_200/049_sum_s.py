# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []
        low, high = 1, 2
        result = []
        while low < high and high < tsum:
            tmp = (low+high)*(high-low+1) / 2
            if tmp == tsum:
                s1 = [i for i in range(low, high+1)]
                result.append(s1)
                low += 1
                high += 1
            elif tmp < tsum:
                high += 1
            else:
                low += 1
        return result

if __name__ == "__main__":
    s = Solution()
    print s.FindContinuousSequence(100)
