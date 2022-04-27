func twoSum(nums []int, target int) []int {
    // make a map, key = [num[i]]; value = index
    kvmap := make(map[int]int)
       
    for i:=0; i<len(nums); i++ {
        desired := target - nums[i]
        index, exist := kvmap[desired]
        if exist {
            if i != index {
                return []int{index, i}    
            }
        }
        kvmap[nums[i]] = i
    }
            
    return []int{0, 0}
}