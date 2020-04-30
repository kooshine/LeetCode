# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        m = len(s)
        if m == 0:
            return False
        sign, hasE, point = False, False, False
        for i in range(m):
            if s[i] == "E" or s[i] == "e":
                if hasE:
                    return False
                if i  == m-1:
                    return False
                hasE = True
            elif s[i] == ".":
                if point or hasE:
                    return False
                if i == 0 or i == m-1:
                    return False
                point = True
            elif s[i] == "+" or s[i] == "-":
                if sign and s[i-1] != "E" and s[i-1] != "e":
                    return False
                if not sign and i != 0 and s[i-1] != "E" and s[i-1] != "e":
                    return False
                sign = True
            elif s[i] > "9" or s[i] < "0":
                return False
        return True
        """
        import re
        return bool(re.match(r'\s*[+-]?([\d]+(\.[\d]*)?|\.[\d]+)(e[+-]?[\d]+)? *$', s))
        """
if __name__ == "__main__":
    s = Solution()
    print s.isNumeric("+100")
