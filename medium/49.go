func groupAnagrams(strs []string) [][]string {
    // make map of slices to hold anagrams
	// k = array26; v = slice of anagrams
	ansmap := make(map[[26]int][]string)
	
	// make array of 26 values representing letters
	var charmap [26]int

	// iterate over strings
	for _, v := range strs {
		// Reset char map
		for i, _ := range charmap {
			charmap[i] = 0
		}

		tmp := []rune(v)
		for _, x := range tmp {
			charmap[x - []rune("a")[0]] += 1
		}
		ansmap[charmap] = append(ansmap[charmap], v)
	}
	
	final_answer:= make([][]string, 0)

	for _, v := range ansmap {
		final_answer = append(final_answer, v)
	}
	
	return final_answer
}