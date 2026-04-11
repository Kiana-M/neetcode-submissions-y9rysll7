class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check:
        for row in board:
            digits = {'1':0, '2':0, '3':0, '4':0,
            '5':0, '6':0, '7':0, '8':0, '9':0, '0':0}
            for element in row:
                if element == '.':
                    continue
                elif digits[element]== 0:
                    digits[element] += 1
                elif digits[element] >= 1:
                    return False
            
        for i in range(len(board[0])):
            digits = {'1':0, '2':0, '3':0, '4':0,
            '5':0, '6':0, '7':0, '8':0, '9':0, '0':0}
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                elif digits[board[j][i]]== 0:
                    digits[board[j][i]] += 1
                elif digits[board[j][i]] >= 1:
                    return False
        
        i,j = 0, 0

        while i<9 and j<9:
            digits = {'1':0, '2':0, '3':0, '4':0,
            '5':0, '6':0, '7':0, '8':0, '9':0, '0':0}
            for p in range(3):
                for q in range(3):
                    if board[i+p][j+q] == '.':
                        continue
                    elif digits[board[i+p][j+q]]== 0:
                        digits[board[i+p][j+q]] += 1
                    elif digits[board[i+p][j+q]] >= 1:
                        return False
            i += 3
            j += 3

        return True
                    


                
        