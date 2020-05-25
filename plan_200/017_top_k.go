package main

import (
    "fmt"
)

func smallestK(arr []int, k int) []int {
    //bubble_sort(arr)
    if k == 0 {
        return nil
    }
    if len(arr) < k {
        return nil
    }
    ret := arr[:k]
    for i := k; i < len(arr); i++ {
        max_val, index := get_max(ret)
        if index >= 0 && arr[i] < max_val {
            ret[index] = arr[i]
        }
    }
    return ret
}
//get_max
func get_max(arr []int) (int, int) {
    if len(arr) == 0 {
        return -1, -1
    }
    tmp := arr[0]
    index := 0
    for i := 1; i < len(arr); i++ {
        if arr[i] > tmp {
            tmp = arr[i]
            index = i
        }
    }
    return tmp, index
}

func main() {
    arr := []int{1,3,5,7,2,4,6,8}
    ret := smallestK(arr, 4)
    fmt.Println(ret)
}
