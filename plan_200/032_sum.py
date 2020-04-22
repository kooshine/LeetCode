# -*- coding: utf-8 -*-

"""
# -*- coding:utf-8 -*-

class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            temp = (num1 ^ num2) & 0xFFFFFFFF
            num2 = ((num1 & num2) << 1) & 0xFFFFFFFF
            num1 = temp
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)
"""
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, a, b):
        while(b):
            a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)
"""
"""

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp
        return num1

if __name__ == "__main__":
    s = Solution()
    print s.Add(12, 7)
