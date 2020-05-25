package main

import (
    "fmt"
)

func oneEditAway(first string, second string) bool {
    len_a := len(first)
    len_b := len(second)
    if len_a - len_b > 1 || len_a -len_b < -1 {
        return false
    }
    if len_a == len_b {
        count := 0
        for i := 0; i < len_a; i++ {
            if first[i] != second[i] {
                count += 1
                if count > 1{
                    return false
                }
            }
        }
    } else {
        if len_a > len_b { //从短的开始比较, 插入一个字符是否相同
            first, second = second, first
            fmt.Println("?")
        }
        fmt.Println(first, second)
        for i := 0; i < len(first); i++ {
            if first[i] != second[i]{
                if i+1 < len_a && first[i+1] != second[i] {
                    return false
                }
            }
        }
    }
    return true
}

func main() {
    fmt.Println(oneEditAway("x", ""))
}
