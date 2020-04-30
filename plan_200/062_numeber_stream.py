# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stream = []
    def Insert(self, num):
        # write code here
        #插入排序
        m = len(self.stream)
        if m == 0:
            self.stream.append(num)
            return
        loc = m
        for i in range(m):
            if self.stream[i] > num:
                loc = i
                break
        self.stream.append(0)
        for i in range(m, loc-1, -1):
            self.stream[i] = self.stream[i-1]
        self.stream[loc] = num
        print self.stream
    def GetMedian(self):
        # write code here
        m = len(self.stream)
        if m == 0:
            return -1
        if  m % 2:
            return self.stream[m/2]
        else:
            mid1 = m / 2
            mid2 = m / 2 -1
            return float(self.stream[mid1] + self.stream[mid2]) / 2

if __name__ == "__main__":
    s = Solution()
    s.Insert(1)
    print s.GetMedian()
    s.Insert(2)
    print s.GetMedian()
    s.Insert(3)
    print s.GetMedian()
    s.Insert(1)
    print s.GetMedian()
