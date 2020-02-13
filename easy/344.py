class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        index = 0
        last_elem = len(s)
        for char in s:
            last_elem -= 1
            tmp = s[last_elem]
            s.pop(last_elem)
            s.append(tmp)
        return s
