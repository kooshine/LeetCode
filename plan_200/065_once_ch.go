package main

import (
    "fmt"
)

func isUnique(astr string) bool {
    flag := map[string]int{}

    for _, val := range astr {
        if _, ok := flag[string(val)]; ok {
            return false
        } else {
            flag[string(val)] = 1
        }
    }
    return true
}
/*
func main() {
    fmt.Println(isUnique("abc"))
}
*/
