# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            if not ((s[start] >= "a" and s[start] <= "z") or (s[start] >= "0" and s[start] <= "9")):
                start += 1
                continue
            if not ((s[end] >= "a" and s[end] <= "z") or (s[end] >= "0" and s[end] <= "9")):
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1

        return True





if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome("0P")
    print s.isPalindrome("A man, a plan, a canal: Panama")
