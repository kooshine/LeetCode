# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/valid-palindrome-ii/


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """timeout
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                if not (self.helper(s, start, end-1) or self.helper(s, start+1, end)) :
                    return False

            start += 1
            end -= 1

        return True

    def helper(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
        """
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        flag = 0
        while start < end:
            if s[start] != s[end]:
                flag += 1
                if flag == 2:
                    return False
                if self.helper(s, start, end-1):
                    end -= 1
                    continue
                elif self.helper(s, start+1, end):
                    start += 1
                    continue
                else:
                    return False

            start += 1
            end -= 1

        return True

    def helper(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
if __name__ == "__main__":
    s = Solution()
    #print s.validPalindrome("aba")
    #print s.validPalindrome("abca")
    #print s.validPalindrome("atbbga")
    #print s.validPalindrome("eeccccbebaeeabebccceea")
    print s.validPalindrome("ebcbbececabbacecbbcbe")
    print s.validPalindrome("ebcbbececabbacecbbcbe")

