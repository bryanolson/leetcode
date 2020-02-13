class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        tmp_list = []
        for item in A:
            tmp_list.append(item[::-1])

        for item in tmp_list:
            for _ in range(len(item)):
                if item[_] == 0:
                    item[_] = 1
                else:
                    item[_] = 0

        return(tmp_list)
