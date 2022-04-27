func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    smap := make(map[byte]int)
    tmap := make(map[byte]int)
    for i := 0; i < len(s); i++ {
        smap[s[i]] += 1
        tmap[t[i]] += 1
    }
    for k, v := range smap {
        if tmap[k] != v {
            return false
        }
    }
    return true
}