class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            sett = set()
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    if element in sett:
                        return False
                    sett.add(element)
    
        # check column
        for i in range(9):
            sett = set()
            for j in range(9):
                element = board[j][i]
                if element != ".":
                    if element in sett:
                        return False
                    sett.add(element)

        # check the nine 3x3 sub-boxes
        possibleStarts = [(0,0), (0, 3), (0,6 ), (3,0), (3,3), (3,6),(6,0), (6,3), (6,6)]
        for i, j in possibleStarts:
            sett = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    element = board[row][col]
                    if element != ".":
                        if element in sett:
                            return False
                        sett.add(element)

        return True