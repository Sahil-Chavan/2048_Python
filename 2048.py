import copy

class Game():
    def __init__(self,board_size,game_type):
        n = int(board_size)*4
        # self.Grid = [[0]*n for _ in range(n)]
        self.Grid = [[0,7,0,0],[4,0,4,2],[4,4,0,2],[8,8,4,4]]
        self.Provide_options()
        
    @staticmethod
    def Display_board(grid):
        print('')
        print('\n\n'.join([' '.join(['{:5}'.format(item) for item in row]) for row in grid]))
   
    def Provide_options(self):
        # print('options:')
        # option = int(input)
        self.Make_move(0)
    
    def Make_move(self,option):
        
        self.New_Grid = copy.deepcopy(self.Grid)
        ## changes in grid
        self.New_Grid = Game.Merge_right_matrix(self.New_Grid)
        
        Game.Display_board(self.Grid)
        print('-'*20)
        Game.Display_board(self.New_Grid)
        print(self.New_Grid==self.Grid)
        
        # if self.New_Grid==self.Grid:
        #     print('\tINVALID MOVE ! - Since it causes no changes in the grid \n \tProvide with new option')
        #     Game.Display_board(self.Grid)
        #     # self.Provide_options()
        # else:
        #     self.Grid = copy.deepcopy(self.New_Grid)
        #     # print(self.Grid)
        #     Game.Display_board(self.Grid)
            
    @staticmethod
    def Merge_left_matrix(grid):
        for r in grid:
            temp_row = list(filter(lambda x: x!=0, r))[:]
            new_row = list()
            while temp_row:
                curr_val = temp_row.pop(0)
                if not temp_row: 
                    new_row.append(curr_val)
                elif curr_val==temp_row[0]:
                    temp_row.pop(0)
                    new_row.append(curr_val*2)
                else:
                    new_row.append(curr_val)
            new_row.extend([0 for _ in range(len(r)-len(new_row))])
            r[:] = new_row[:]
        return grid
    
    def Merge_right_matrix(grid):
        grid_r =  [list(reversed(l)) for l in grid]
        # print(grid_r)
        grid_l = Game.Merge_left_matrix(grid_r)
        print(grid_l)
        return [list(reversed(l)) for l in grid_l]
    
                
                   
           
        
        
if __name__ == '__main__':
    # game = Game(1,'NA')
    # game.Display_board()
    
    # print([[1,2,3],[1,4,5]]==[[1,2,3],[1,4,5]])
    Grid = [[0,7,0,0],[4,0,4,2],[4,4,0,2],[8,8,4,4]]
    b = list()
    for a in zip(*Grid):
        b.append(list(a))
    b.reverse() 
    for c in b:
        print(c)
