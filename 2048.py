

class Game():
    def __init__(self,board_size,game_type):
        n = int(board_size)*4
        self.Grid = [[0]*n for _ in range(n)]

    @staticmethod
    def Display_board(grid):
        print('')
        print('\n\n'.join([' '.join(['{:5}'.format(item) for item in row]) for row in grid]))
   
    def Provide_options(self):
        print('options:')
        option = int(input)
        self.Make_move(option)
    
    def Make_move(self,option):
        self.New_Grid = self.Grid.copy()
        ## changes in grid
        if self.New_Grid==self.Grid:
            print('\t\t INVALID MOVE ! - Since it causes no changes in the grid')
            self.Move()
        else:
            self.Grid = self.New_Grid
            Game.Display_board(self.Grid)
            
    def Merge_left_matrix(grid):
       for r in grid:
           temp_row = r.copy()
           
        
        
if __name__ == '__main__':
    game = Game(2,'NA')
    game.Display_board()
