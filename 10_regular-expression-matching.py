# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/regular-expression-matching/


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        first_match = bool(s) and p[0] in [s[0], "_"]

        if len(p) >= 2 and p[1] == "*":
            return (self.isMatch(s, p[2:]) #0 的情况
                    or first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        return True

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("mississippi", "mis*is*p*.")
