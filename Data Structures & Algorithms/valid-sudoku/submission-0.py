class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=[{} for _ in range (len(board))]
        row=[{} for _ in range (len(board[0]))]
        square=[[{} for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range (len(board[0])):
                if board[i][j] in col[j] and board[i][j]!="." :
                    return False
                else:
                    col[j][board[i][j]]=1
                if board[i][j] in row[i] and board[i][j]!=".":
                    return False
                else:
                    row[i][board[i][j]]=1

                if board[i][j] in square[i//3][j//3] and board[i][j]!="." :
                    return False
                else:
                    square[i//3][j//3][board[i][j]]=1
        return True
