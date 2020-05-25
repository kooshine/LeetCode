package main

import (
    "fmt"
    "strings"
    "sort"
)

func arrangeWords(text string) string {
    text = strings.ToLower(text)
    t_s := strings.Split(text, " ")
    len_s := make([]int, len(t_s))
    for i, v := range t_s {
        len_s[i] = len(v)
    }
    //quick_sort by len_s
    //quick_sort()
    sort.Slice(len_s, func(a, b int) bool{
        /*
        if len_s[a] > len_s[b] {
            t_s[a], t_s[b] = t_s[b], t_s[a]
        }
        */
        return len_s[a] < len_s[b]
    })
    fmt.Println(len_s)
    //result := make([]string, len(t_s))
    result := []string{}
    for i := 0; i < len(len_s); i++ {
        index := 0
        for index < len(t_s) {
            if len(t_s[index]) == len_s[i] {
                result = append(result, t_s[index])
                t_s = append(t_s[:index], t_s[index+1:]...)
                break
            }
            index++
        }
    }
    //tmp := []rune(t_s[0])
    tmp := []rune(result[0])
    if string(tmp[0]) >= string("A") && string(tmp[0]) <= string("Z") {
        ret := strings.Join(t_s, " ")
        return ret
    }
    tmp[0] = tmp[0] - 32
    result[0] = string(tmp)
    ret := strings.Join(result, " ")
    return ret
}

func main() {
    //test := "Leetcode is ccoolcool"
    test := "Jtik hrzrvhbmk gbo cfhmiqwonj ojkew ufvledv bomoeqt ops jgi zdhvbpbb zczmepdfpm jry rjazc titttcu"
    ret := arrangeWords(test)
    fmt.Println(ret)
}
