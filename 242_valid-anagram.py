# -*- coding: utf-8 -*-

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        s = str(s)
        t = str(t)
        s1 = [s[i] for i in range(len(s))]
        t1 = [t[i] for i in range(len(t))]
        s1.sort()
        t1.sort()
        print s1, t1

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        """
        return sorted(s) == sorted(t)
if __name__ == "__main__":
    s = Solution()
    print s.isAnagram("anagram", "nagaram")
