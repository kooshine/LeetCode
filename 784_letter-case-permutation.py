# -*- coding: utf-8 -*-
#https://leetcode-cn.com/problems/letter-case-permutation/
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        size = len(S)
        path = []
        result = []
        start = 0
        self.dfs(S, path, result, start, size)
        return result

    def dfs(self, S, path, result, start, size):
        if start == size:
            result.append("".join(path))
            return
        #for index in range(start, size):
        if S[start] >= 'a' and S[start] <= 'z':
            path.append(S[start].upper())
            self.dfs(S, path, result, start+1, size)
            path.pop()
        if S[start] >= 'A' and S[start] <= 'Z':
            path.append(S[start].lower())
            self.dfs(S, path, result, start+1, size)
            path.pop()

        path.append(S[start])
        self.dfs(S, path, result, start+1, size)
        path.pop()

        """
        size = len(S)
        index = 0
        result = []
        self.dfs(result, S, index, size)
        return list(set(result))

    def dfs(self, result, S, index, size):
        if index == size:
            return
        result.append(S)
        if S[index] >= 'a' and S[index] <= 'z':
            tmp = S[:index] + S[index].upper() + S[index+1:]
            result.append(tmp)
            self.dfs(result, tmp, index+1, size)
        if S[index] >= 'A' and S[index] <= 'Z':
            tmp = S[:index] + S[index].lower() + S[index+1:]
            result.append(tmp)
            self.dfs(result, tmp, index+1, size)

        self.dfs(result, S, index+1, size)
        """
if __name__ == "__main__":
    s = Solution()
    print s.letterCasePermutation("a1b2")
