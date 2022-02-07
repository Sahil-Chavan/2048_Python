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
        self.New_Grid = Game.Merge_down_matrix(self.New_Grid)
        
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
        for row in grid:
            temp_row = list(filter(lambda x: x!=0, row))[:]
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
            new_row.extend([0 for _ in range(len(row)-len(new_row))])
            row[:] = new_row[:]
        return grid
    
    @staticmethod
    def Merge_right_matrix(grid):
        grid_r =  [list(reversed(l)) for l in grid]
        grid_l = Game.Merge_left_matrix(grid_r)
        return [list(reversed(l)) for l in grid_l]
    
    @staticmethod
    def Merge_up_matrix(grid):
        grid_u = list()
        for row in zip(*grid):
            grid_u.append(list(row)) 
        grid_u.reverse()
        grid_l = Game.Merge_left_matrix(grid_u)
        grid_l.reverse()
        grid_u = list()
        for row in zip(*grid_l):
            grid_u.append(list(row)) 
        return grid_u
    
    @staticmethod
    def Merge_down_matrix(grid):
        grid_d = list()
        for row in zip(*grid):
            grid_d.append(list(row)) 
        grid_d = [list(reversed(l)) for l in grid_d]
        grid_l = Game.Merge_left_matrix(grid_d)
        grid_l = [list(reversed(l)) for l in grid_l]
        grid_d = list()
        for row in zip(*grid_l):
            grid_d.append(list(row)) 
        return grid_d
        
                   
           
        
        
if __name__ == '__main__':
    board_size = input('\tPlease select Grid size : \n\t 1) 4 X 4 Grid \n\t 2) 8 X 8 Grid')
    game = Game(board_size,0)
    # game.Display_board()
    
    # print([[1,2,3],[1,4,5]]==[[1,2,3],[1,4,5]])
    # Grid = [[0,7,0,0],[4,0,4,2],[4,4,0,2],[8,8,4,4]]
    # b = list()
    # for a in zip(*Grid):
    #     b.append(list(a))
    # b = [list(reversed(l)) for l in b]
    # for c in b:
    #     print(c)
