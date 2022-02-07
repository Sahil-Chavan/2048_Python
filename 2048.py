import copy
from random import sample

class Game():
    def __init__(self,game_type):
        
        self.Board_size = Game.Collect_size()
        self.Grid = [[0]*self.Board_size for _ in range(self.Board_size)]
        self.Random_add()
        # self.Grid = [[0,7,0,0],[4,0,4,2],[4,4,0,2],[8,8,4,4]]
        self.Provide_options()
    
    @staticmethod
    def Collect_size():
        got_option = False
        board_size = 1
        while not got_option:
            board_size = int(input('\tPlease select Grid size : \n\t 1) 4 X 4 Grid \n\t 2) 8 X 8 Grid \n\t'))
            if not Game.Check_options(2,board_size):
                print('\tINVALID OPTION !')
            else:
                got_option = True 
                break
        return board_size*4
        
    @staticmethod
    def Collect_move():
        got_option = False
        msessage = '\tSelect the move you want to make : \n\t   1) Slide Left \n\t   2) Slide Right \n\t   3) Slide Up \n\t   4) Slide Down \n\t   5) Exit \n\t '

        while not got_option:
            option = int(input(msessage))
            if not Game.Check_options(5,option):
                print('\tINVALID OPTION !')
            else:
                got_option = True 
                break
        if option==5: 
            print('\tThank you for playing !')
            exit()
        return option
    
    @staticmethod
    def Display_board(grid):
        print('')
        print('\n\n'.join([' '.join(['{:5}'.format(item) for item in row]) for row in grid]))
   
    def Provide_options(self,with_random_add =True):
        if with_random_add:self.Random_add()
        Game.Display_board(self.Grid)
        option = Game.Collect_move()
        self.Make_move(option)
    
    def Make_move(self,option):
        
        self.New_Grid = copy.deepcopy(self.Grid)
        
        Function_map = {1:Game.Merge_left_matrix,2:Game.Merge_right_matrix,3:Game.Merge_up_matrix,4:Game.Merge_down_matrix}
        self.New_Grid = Function_map[option](self.New_Grid)
        
        # self.New_Grid = Game.Merge_down_matrix(self.New_Grid)
        
        # Game.Display_board(self.Grid)
        # print('-'*20)
        # Game.Display_board(self.New_Grid)
        # print(self.New_Grid==self.Grid)
        
        if self.New_Grid==self.Grid:
            print('\tINVALID MOVE ! - Since it causes no changes in the grid \n \tProvide with new option')
            # Game.Display_board(self.Grid)
            self.Provide_options(False)
        else:
            self.Grid = copy.deepcopy(self.New_Grid)
            self.Provide_options()
            # Game.Display_board(self.Grid)
            
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
    
    def Random_add(self):
        flat_grid = [item for row in self.Grid for item in row]
        zero_indexes = [i for i,v in enumerate(flat_grid) if v==0]
        add_index = sample(zero_indexes,1)[0]
        row_index = add_index//self.Board_size
        col_index = add_index%self.Board_size
        rand_val = sample([2,4],1)[0]
        self.Grid[row_index][col_index] = rand_val
        
    @staticmethod    
    def Check_options(extent,current_option):
        return current_option in list(range(1,extent+1))
        
                   
           
        
        
if __name__ == '__main__':
    game = Game(0)
    
    # print([[1,2,3],[1,4,5]]==[[1,2,3],[1,4,5]])
    # Grid = [[0,7,0,0],[4,0,4,2],[4,4,0,2],[8,8,4,4]]
    # print([item for row in Grid for item in row])
    # flat_grid = [item for row in Grid for item in row]
    # zero_indexes = [i for i,v in enumerate(flat_grid) if v==0]
    # print(zero_indexes)
    # print(sample(zero_indexes,1))
    # b = list()
    # for a in zip(*Grid):
    #     b.append(list(a))
    # b = [list(reversed(l)) for l in b]
    # for c in b:
    #     print(c)
    

    
