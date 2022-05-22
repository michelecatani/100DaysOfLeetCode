class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        theLength = len(mat)
        
        theSum = 0
        
        i = 0
        
        while i < theLength:
            theSum += mat[i][i]
            i += 1
        
        i = 0
        j = len(mat) - 1
        
        while i < theLength:
            if i != j:
                theSum += mat[i][j]
            i += 1
            j -= 1
        
        return theSum
            