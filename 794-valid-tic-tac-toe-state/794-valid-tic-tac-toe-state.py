import operator

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        b = "|".join(board)
        def check_winner(b,p):
            
            #check row
            if p*3 in b.split("|"):
                return True
            # check column
            for i in range(3):
                if p*3 in b[i::4]:
                    return True
            #check left diagonal
            if p*3 in b[::5]:
                return True
            #check right diagonal
            if p*3 in b[2::3]:
                return True
            return False
        
        m = b.count("X")-b.count("O")
        return (m == 0 and not check_winner(b,"X")) or (m == 1 and not check_winner(b,"O"))
        