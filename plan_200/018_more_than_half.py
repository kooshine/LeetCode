# -*- coding: utf-8 -*-

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        """
        statics = dict()
        m = len(numbers)

        for i in range(m):
            if numbers[i] in statics:
                statics[numbers[i]] += 1
            else:
                statics[numbers[i]] = 1
            print statics
            if statics[numbers[i]] > m/2:
                return numbers[i]
        return 0
        """

if __name__ == "__main__":
    s = Solution()
    print s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])
