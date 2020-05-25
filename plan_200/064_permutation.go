//package main
import (
    "fmt"
)
func permutation(S string) []string {
    result := []string{}
    dfs(S, "", &result)
    return result
}
func dfs(S string, path string, result *[]string) {
    if len(S) == 0 {
        *result = append(*result,path)
    }
    for i, _ := range S {
        s := []rune(S)
        cur := s[i]
        s = append(s[:i], s[i+1:]...)
        dfs(string(s), path + string(cur), result)
    }
    return
}
/*
func permutation(S string) []string {

	res:=[]string{}
	helpPermutation(S,"",&res)
	return res
}
//每次从S中拿出一个字符 放到path字符串中，最后 S==""全部拿完了，由于 for循环中每次拿出的i的变化的。遍历了所有可能，比如 当S一个字符都没有拿的时候，从 第0个字符 到第 len-1个字符 有n中可能，然后这n中可能里面 每一种又有 n-1种可能 都遍历到了
func helpPermutation(S string,path string,res *[]string){
	if S==""{
		*res= append(*res, path)
	}

	for i:=0;i< len(S);i++{

		s:=[]rune(S)
		cur:=s[i]
		if i< len(s)-1{
			s= append(s[:i], s[i+1:]...)
		}else{
			s=s[:i]
		}
		helpPermutation(string(s),path+string(cur),res)

	}
	return
}
*/
func main(){
    S := "pwe"
    result := permutation(S)
    fmt.Println(result)
}
