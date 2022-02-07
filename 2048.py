

class Python_2048():
    def __init__(self,board_size,game_type):
        n = int(board_size)*4
        self.GRID = [[0]*n for _ in range(n)]

    def Display_board(self):
        print('')
        print('\n\n'.join([' '.join(['{:5}'.format(item) for item in row]) for row in self.GRID]))
        
    # def Merge_right_row():
        
if __name__ == '__main__':
    game = Python_2048(2,'NA')
    game.Display_board()
