# -*- coding: utf-8 -*-

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            if array[i][0] > target or array[i][-1] < target:
                continue
            #二分查找
            start = 0
            end = len(array[i])
            while start < end:
                mid = (start + end) / 2
                if array[i][mid] < target:
                    start = mid + 1
                elif array[i][mid] > target:
                    end  = mid -1
                else:
                    return 1
        return 0

if __name__ == "__main__":
    s = Solution()
    target = 5
    array = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
    print s.Find(target, array)
