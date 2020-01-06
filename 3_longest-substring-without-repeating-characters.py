# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N == 0:
            return 0
        start = 0
        end = 1
        max_len = 1
        tmp = ""
        for i in range(1, N):
            tmp = s[start:end]
            if s[i] not in tmp:
                end = i+1
                if end - start > max_len:
                    max_len = end-start
            else:
                for j in range(len(tmp)):
                    if s[i] == tmp[j]:
                        start = start + j+1
                        end += 1

        return max_len


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("au")
    print s.lengthOfLongestSubstring("dvdf")
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("pwwkew")
    print s.lengthOfLongestSubstring("bbtablud")
