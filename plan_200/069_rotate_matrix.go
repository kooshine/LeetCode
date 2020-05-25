package main
import (
    "fmt"
)
func rotate(matrix [][]int)  {
    rows := len(matrix)
    if rows == 0 {
        return
    }

    for i := 0; i < rows/2; i++ {
        for j:= i; j < rows-1-i; j++ {
            tmp := matrix[i][j]
            matrix[i][j] = matrix[rows-1-j][i]
            matrix[rows-1-i][rows-1-j] = matrix[j][rows-1-i]
            matrix[j][rows-i-1] = tmp
        }
    }
}
func main() {
    matrix := [][]int{
        {1,2,3,4},
        {5,6,7,8},
        {9,10,11,12},
        {13,14,15,16},
    }
    rotate(matrix)
    fmt.Println(matrix)
}
