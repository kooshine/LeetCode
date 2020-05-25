package main

import (
    "fmt"
)

func findLadders(beginWord string, endWord string, wordList []string) []string {
    if len(wordList) == 0 {
        return []string{}
    }
    visited := make(map[string]bool)
    path := []string{beginWord}
    return dfs(beginWord, endWord, 0, path, wordList, visited)
}
func dfs(beginWord, endWord string, index int, path, wordList []string, visited map[string]bool) []string {
    if beginWord == endWord {
        return path
    }
    if index >= len(wordList) {
        return nil
    }
    if _, ok := visited[beginWord]; ok {
        return nil
    }
    for i := index; i < len(wordList); i++ {
        if !onlyOneDifference(wordList[i], beginWord) {
            continue
        }
        t := wordList[i]
        wordList[i], wordList[index] = wordList[index], wordList[i]
        newPath := make([]string, len(path))
        copy(newPath, path)
        newPath = append(newPath, t)
        result := dfs(t, endWord, index+1, newPath, wordList, visited)
        if result != nil {
            return result
        }
        wordList[i], wordList[index] = wordList[index], wordList[i]
        visited[t] = true
    }
    return nil
}
func onlyOneDifference(s1,s2 string) bool {
    diff := 0
    for i := 0; i < len(s1); i ++ {
        if s1[i] != s2[i] {
            diff++
            if diff > 1 {
                return false
            }
        }
    }
    if diff == 1 {
        return true
    }
    return false
}

func main() {
    wordList := []string{"hot", "dot", "dog", "lot", "log", "cog"}
    ret := findLadders("hit", "cog", wordList)
    fmt.Println(ret)
}
