class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        col_set = [set() for x in range (n)] 
        
        for r in range (n):

            row_set = set()

            if r%3 == 0:
                sub_set = [set() for x in range (3)]

            for c in range (n):

                if board[r][c] == ".":
                    continue 
                if (board[r][c] in row_set) or (board[r][c] in col_set[c]) or (board[r][c] in sub_set[c//3]):
                    return False

                row_set.add(board[r][c])
                col_set[c].add(board[r][c])   
                sub_set[c//3].add(board[r][c])     

        return True     