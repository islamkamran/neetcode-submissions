class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # steps to solve
        # 1. empty spaces are '.'
        # 2. make dictionaries collection.defaultmap(set)
        # 3. make harcoded double loop i and j and limit is 9 as given in task
        # 4. check current item i,j with row duplicate set or column duplicate set or the range of sub squre duplicate set
        # 5. if passes all return true

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
        

        