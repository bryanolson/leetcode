class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_arr = [char for char in J]
        s_arr = [char for char in S]
        counter = 0
        
        for item in s_arr:
            if item in j_arr:
                counter +=1
        
        return counter
