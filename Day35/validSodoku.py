class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            theSet = set(num for num in range(1, 10))
            for j in i:
                if j != '.':
                    if int(j) not in theSet:
                        return False
                    theSet.remove(int(j))
        
        for i in range(len(board)):
            theSet = set(num for num in range(1, 10))
            for j in range(len(board)):
                if board[j][i] != '.':
                    if int(board[j][i]) not in theSet:
                        return False
                    theSet.remove(int(board[j][i]))
        
        for i in range(3): 
            for j in range(3):
                theSet = set(num for num in range(1, 10))
                for z in range(0, 3):
                    for q in range(0, 3):
                        if board[3 * i + z][3 * j + q] != '.':
                            if int(board[3 * i + z][3 * j + q]) not in theSet:
                                return False
                            theSet.remove(int(board[3 * i + z][3 * j + q]))
        
        return True