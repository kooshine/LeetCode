# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/lemonade-change/submissions/

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        result = True
        if bills == [] or bills[0] != 5:
            return False

        five, ten = 0, 0
        for item in bills:
            if item == 5:
                five += 1
            if item == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    result = False
                    return result
            if item == 20:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    result = False
                    return result

        return result

if __name__ == "__main__":
    s = Solution()
    print s.lemonadeChange([5,5,10,10,20])
