class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row and then column
        # top to bottom is row and left to right is column

        ROWS, COLS = len(matrix), len(matrix[0])
        top_row, bot_row = 0, ROWS - 1

        while top_row <= bot_row:
            row = (top_row + bot_row) // 2
            if target > matrix[row][-1]:
                top_row = row + 1
            elif target < matrix[row][0]:
                bot_row = row - 1
            else:
                break
        
        # here occurs two cases either break reached or loop finished with out any loop.
        # Now we only found the target range loop not sure if the target element will be there or no.

        if not top_row <= bot_row:
            return False

        lp, rp = 0, COLS - 1

        while lp <= rp:
            mid_point = (lp + rp) // 2

            if target > matrix[row][mid_point]:
                lp = mid_point + 1
            elif target < matrix[row][mid_point]:
                rp = mid_point - 1
            else:
                return True
        return False


