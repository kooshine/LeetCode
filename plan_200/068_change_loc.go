package main

import (
    "fmt"
)
func groupAnagrams(strs []string) [][]string {
    ret := make(map[string][]string)
    for _, val := range strs{
        tmp := sort(val)
        if _, ok := ret[tmp]; ok {
            ret[tmp] = append(ret[tmp], val)
        } else {
            ret[tmp] = []string{val}
        }
    }
    result := make([][]string, 0)
    for _, val := range ret {
        /*
        tmp := make([]string, 0)
        for _, v := range val {
            tmp = append(tmp, v)
        }
        result = append(result,tmp)
        */
        result = append(result,val)
    }
    return result
}
func sort(s string) string {
    strs := []rune(s)
    for i := 0; i < len(strs); i++ {
        for j := i+1; j < len(strs); j++ {
            if strs[j] < strs[i] {
                strs[j], strs[i] = strs[i], strs[j]
            }
        }
    }
    return string(strs)
}
func main() {
    strs := []string{"eat", "ate", "tan", "tea", "nat", "bat"}
    fmt.Println(groupAnagrams(strs))
}
