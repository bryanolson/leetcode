func productExceptSelf(nums []int) []int {
    final_ans := make([]int, len(nums))
	for i := range final_ans {
		final_ans[i] = 1
	}
	// prefix pass
	prefix := 1
	for i, v := range nums {
		final_ans[i] *= prefix
		prefix *= v
	}

	postfix := 1
	// postfix pass
	for i:=len(nums)-1; i >= 0; i-- {
		final_ans[i] *= postfix
		postfix *= nums[i]
	}

	return final_ans
}