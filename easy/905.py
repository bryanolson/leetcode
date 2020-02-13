class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        tmp_list = []

        for item in A:
            if item%2 == 0:
                tmp_list.append(item)
        for item in A:
            if item%2 >= 1:
                tmp_list.append(item)
        return(tmp_list)
