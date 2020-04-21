# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, index):
            tmp = self.get_min(ugly[i2] * 2, self.get_min(ugly[i3] * 3, ugly[i5] * 5))
            print tmp
            ugly.append(tmp)
            if tmp == ugly[i2] * 2:
                i2 += 1
            if tmp == ugly[i3] * 3:
                i3 += 1
            if tmp == ugly[i5] * 5:
                i5 += 1
            print i2, i3, i5
        print ugly
        return ugly[index-1]

    def get_min(self, a, b):
        return a if a < b else b

if __name__ == "__main__":
    s =Solution()
    print s.GetUglyNumber_Solution(10)
