func topKFrequent(nums []int, k int) []int {    
    var ans []int
    length := len(nums)+1
    freq_list := make([][]int, length)
    
    for i := range(freq_list) {
        freq_list[i] = make([]int, 0)
    }
    
    // make map of frequency of each term\
    // k = int, v = frequency
    freq := make(map[int]int)
    
    for i:=0;i<len(nums);i++ {
        freq[nums[i]] += 1
    }
    
    // loop k, v in map, append to list where index = frequency
    for k, v := range freq {
        freq_list[v] = append(freq_list[v], k)
    }
    
    // loop list backwards until k elements are found
    for i := len(freq_list)-1; i > -1; i-- {
		if len(freq_list[i]) != 0 {
			if len(ans) == k {
				return ans
			}
			for _, x := range freq_list[i] {
				ans = append(ans, x)
			}                
		}
    }
    return ans
}