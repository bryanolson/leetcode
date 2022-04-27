func containsDuplicate(nums []int) bool {
    dups := make(map[int]int)
    for _, v := range nums {
        dups[v] += 1
        if dups[v] >= 2 {
            return true
        }
    }
    return false
}