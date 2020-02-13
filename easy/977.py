class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        tmp_list=[]
        for _ in range(len(A)):
            tmp_list.append(A[_]*A[_])
        return sorted(tmp_list)
