# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        """
        if len(tinput) < k:
            return []
        tinput.sort()
        return tinput[:k]
        """
        if len(tinput) < k:
            return []
        array = [tinput[i] for i in range(k) ]
        for i in range(k, len(tinput)):
            maxValue, index = self.getMax(array)
            if tinput[i] < maxValue:
                array[index] = tinput[i]

        array.sort()
        return array

    def getMax(self, array):
        m = len(array)
        if m <= 0:
            return None, None
        maxValue = array[0]
        index = 0
        for i in range(1, m):
            if array[i] > maxValue:
                maxValue = array[i]
                index = i
        return maxValue, index
if __name__ == "__main__":
    s = Solution()
    print s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 0)
