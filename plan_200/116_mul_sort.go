package main
import (
    "fmt"
    "sort"
)
func bestSeqAtIndex(height []int, weight []int) int {
    person := make([][2]int, len(height))

    for i := 0; i < len(height); i++ {
        person[i] = [2]int{height[i], weight[i]}
    }
    sort.Slice(person, func(a, b int) bool {
        if person[a][0] == person[b][0] {
            return person[a][1] > person[b][1]
        }
        return person[a][0] < person[b][0]
    })
    fmt.Println(person)
    p := []int{}
    for i := 0; i < len(height); i++ {
        if len(p) == 0 || (person[i][0] > person[len(p)-1][0] && person[i][1] > person[len(p)-1][1]) {
            p = append(p, i)
        } else {
            start, end := 0, len(p) - 1
            for start < end {
                mid := start + (end - start) / 2
                if person[i][0] > person[p[mid]][0] && person[i][1] > person[p[mid]][1] {
                    start = mid + 1
                } else {
                    end = mid
                }
            }
            p[end] = i
        }
    }
    return len(p)
}

func quick_sort(height []int, weight []int, start, end int) {
    if start < end {
        q := partition(height, weight, start, end)
        quick_sort(height, weight, start, q-1)
        quick_sort(height, weight, q+1, end)
    }
}
func partition(height []int, weight []int, start, end int) int {
    x := height[end]
    i := start-1
    for j := start; j < end; j++ {
        if height[j] < x {
            i += 1
            height[i], height[j] = height[j], height[i]
            weight[i], weight[j] = weight[j], weight[i]
        }
    }
    height[i+1], height[end] = height[end], height[i+1]
    weight[i+1], weight[end] = weight[end], weight[i+1]
    return i+1
}
func main() {
    //height := []int{2868,5485,1356,1306,6017,8941,7535,4941,6331,6181}
    //weight := []int{5042,3995,7985,1651,5991,7036,9391,428,7561,8594}
    height := []int{5,4,3,3,1}
    weight := []int{5,4,6,5,1}
    ret := bestSeqAtIndex(height, weight)
    fmt.Println(height, "\n", weight, ret)
}
