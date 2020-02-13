class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A = sorted(A)
        leng = int(len(A)/2)
        if A[leng] == A[leng+1]:
            return A[leng]
        else:
            return A[leng-1]
        
