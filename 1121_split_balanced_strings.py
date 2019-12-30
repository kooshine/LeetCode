# -*- coding: utf-8 -*-

#贪心算法
#https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        size = len(s)
        i = 0
        while i < size:
            if s[i] == "R":
                r_num = 1
                l_num = 0
                for j in range(i+1, size):
                    if s[j] == "R":
                        r_num += 1
                    else:
                        l_num += 1

                    if l_num == r_num:
                        result += 1
                        print "R::",i, j, s[i:j+1]
                        break
            else:
                r_num = 0
                l_num = 1
                for j in range(i+1, size):
                    if s[j] == "L":
                        l_num += 1
                    else:
                        r_num += 1
                    if l_num == r_num:
                        result += 1
                        break
            i = j+1
        return result
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        cur = 0
        for x in s:
            if x == 'L':
                cur -= 1
            else:
                cur += 1
            if cur == 0:
                res += 1
        return res

作者：larger5
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/solution/python-by-larger5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
if __name__ == "__main__":
    s = Solution()
    print s.balancedStringSplit("RLLLLRRRLR")
    print s.balancedStringSplit("LLLLRRRR")
