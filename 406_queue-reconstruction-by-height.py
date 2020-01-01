# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/queue-reconstruction-by-height/

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        result = []
        if people == []:
            return []
        result.append(people[0])
        for i in range(1, len(people)):
            for j in range(len(result)-1, -1, -1):
                if people[i][0] < result[j][0]:
                    result.insert(j+1, people[i])
                    break
                if people[i][0] == result[j][0]:
                    for k in range(0, len(result)):
                        if people[i][0] == result[k][0] and people[i][1] <= result[k][1]:
                            result.insert(k, people[i])
                            break
                    if people[i] not in result:
                        result.insert(j+1, people[i])
                    break
            if people[i] not in result:
                result.insert(0, people[i])
        #[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        #[[9, 0], [7, 0], [6, 0], [6, 2], [5, 3], [5, 2], [3, 0], [3, 4], [2, 7], [1, 9]]

        for i in range(len(result)):
            index = result[i][1]
            tmp = result[i]
            result.pop(i)
            result.insert(index, tmp)
        return result
        """
        people.sort(key = lambda x: [-x[0], x[1]])
        result = people
        print result
        ret = []
        for i in range(len(result)):
            index = result[i][1]
            ret.insert(index, result[i])
        return ret


if __name__ == "__main__":
    s = Solution()
    print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    print s.reconstructQueue([[1,0],[2,0]])

    print s.reconstructQueue([[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]])
    #print s.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])
