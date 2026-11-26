class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        for i in range(9):
            seen = set()
            for j in range(9):
                cell = board[j][i]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        boxes = {}
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                key = (r // 3, c // 3)
                if key not in boxes:
                    boxes[key] = set()
                if cell in boxes[key]:
                    return False
                boxes[key].add(cell)
        return True
        
            
