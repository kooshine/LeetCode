package main

import (
    "fmt"
)

func findK(matrix [][]int, n, k int) (int, int){
    if n == 0 {
        return -1, -1
    }
    if k > matrix[n-1][n-1] || k < matrix[0][0] {
        return -1, -1
    }
    /*
    for i := 0; i < n; i++ {
        //
        if k > matrix[i][n-1] || k < matrix[i][0] {
            continue
        }
        start, end := 0, n-1
        for start < end {
            mid := start + (end - start) / 2
            fmt.Println(i, mid)
            if k > matrix[i][mid] {
                start = mid+1
            } else {
                end = mid
            }
        }
        return i ,end
    }
    */
    row, col := 0, n-1
    for col >= 0 && row < n {
        if matrix[row][col] > k {
            col -= 1
        } else if matrix[row][col] < k {
            row += 1
        } else {
            return row, col
        }
    }
    return -1, -1
}

func main() {
    var (
        n int
        matrix [][]int
        k int
    )
    fmt.Scanln(&n)
    fmt.Scanln(&k)
    matrix = make([][]int, n)
    for i := 0; i < n; i++ {
        matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            fmt.Scanln(&matrix[i][j])
        }
    }
    /*
    matrix := [][]int{
        {1,2,3,4,5},
        {2,4,6,7,8},
        {3,5,9,10,11},
        {4,6,10, 12, 14},
        {5,7, 11, 13, 16},
    }
    */
    i, j := findK(matrix, n, k)
    fmt.Println(i, j)
}
