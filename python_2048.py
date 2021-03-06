# importing dependencies.
import copy
from datetime import datetime
# from random import sample

class Game():
    # Initializing the constructor
    def __init__(self):
        self.Board_size,self.Game_type = Game.Collect_size()
        self.Grid = [[0]*self.Board_size for _ in range(self.Board_size)]
        self.Random_add()
        # self.Grid = [[8,0,32,0],[2,36,4,16],[16,256,128,8],[36,64,8,4]]
        self.Function_map = {1:Game.Merge_left_matrix,2:Game.Merge_right_matrix,3:Game.Merge_up_matrix,4:Game.Merge_down_matrix }
        self.Provide_options()
    
    # An static method for taking board size and win condition from user.
    @staticmethod
    def Collect_size():
        got_option1 = False
        board_size = 1
        while not got_option1:
            board_size = int(input('\tPlease select Grid size : \n\t 1) 4 X 4 Grid \n\t 2) 8 X 8 Grid \n\t'))
            if not Game.Check_options(2,board_size):
                print('\tINVALID OPTION !')
            else:
                got_option1 = True 
                break
        
        got_option2 = False
        game_type = 1
        while not got_option2:
            game_type = int(input('\tPlease select Grid size : \n\t 1) 2048 \n\t 2) 4096 \n\t'))
            if not Game.Check_options(2,game_type):
                print('\tINVALID OPTION !')
            else:
                got_option2 = True 
                break
            
        return board_size*4,game_type*2048
        
    # An static method for considering the next move from the user.
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
    
    # An static method for displaying the game board.
    @staticmethod
    def Display_board(grid):
        print('')
        print('\n\n'.join([' '.join(['{:5}'.format(item) for item in row]) for row in grid]))
   
    # An method for displaying the the options of possible moves.
    def Provide_options(self,with_random_add =True):
        if with_random_add:self.Random_add()
        self.Verdict()
        Game.Display_board(self.Grid)
        option = Game.Collect_move()
        self.Make_move(option)
    
    #Metho for calling the specific method for specific move and validating the move.
    def Make_move(self,option):
        
        self.New_Grid = copy.deepcopy(self.Grid)
        self.New_Grid = self.Function_map[option](self.New_Grid)
        
        if self.New_Grid==self.Grid:
            print('\tINVALID MOVE ! - Since it causes no changes in the grid \n \tProvide with new option')
            self.Provide_options(False)
        else:
            self.Grid = copy.deepcopy(self.New_Grid)
            
            self.Provide_options()
    
    # Method for checking the Win or Lose conditions.
    def Verdict(self):
        self.Has_won()
        is_empty = False
        for r in range(self.Board_size):
            for c in range(self.Board_size):
                if self.Grid[r][c] == 0:
                    is_empty = True
        if not is_empty:
            self.Has_lost()

    # Method for Losing conditions
    def Has_lost(self):
        test_grid = copy.deepcopy(self.Grid)
        if self.Function_map[1](test_grid)==test_grid:
            if self.Function_map[2](test_grid)==test_grid:
                if self.Function_map[3](test_grid)==test_grid:
                    if self.Function_map[4](test_grid)==test_grid:
                        Game.Display_board(self.Grid)
                        print('\t !!! You Lost !!! \n\t !!! Thank you for playing !!!')
                        exit()
    
    # Method for Wining conditions
    def Has_won(self):
        for r in range(self.Board_size):
            for c in range(self.Board_size):
                if self.Grid[r][c] == self.Game_type:
                    Game.Display_board(self.Grid)
                    print('\t !!! Hurray You Won !!! \n\t !!! Thank you for playing !!!')
                    exit()
        
    # Static Method for computing the matrix after sliding in left direction.
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
    
    # Static Method for computing the matrix after sliding in right direction.
    @staticmethod
    def Merge_right_matrix(grid):
        grid_r =  [list(reversed(l)) for l in grid]
        grid_l = Game.Merge_left_matrix(grid_r)
        return [list(reversed(l)) for l in grid_l]
    
    # Static Method for computing the matrix after sliding in upward direction.
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
    
    # Static Method for computing the matrix after sliding in downward direction.
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
    
    # Method for randomly adding 2 or 4 at an random position in the grid.
    def Random_add(self):
        flat_grid = [item for row in self.Grid for item in row]
        zero_indexes = [i for i,v in enumerate(flat_grid) if v==0]
        # add_index = sample(zero_indexes,1)[0] # This is randomization usind random module.
        index_of_zero_index = (int(datetime.now().strftime("%S"))+len(zero_indexes))%len(zero_indexes) # This is randomization usind datetime module.
        add_index = zero_indexes[index_of_zero_index]
        row_index = add_index//self.Board_size
        col_index = add_index%self.Board_size
        index_of_rand_val = (int(datetime.now().strftime("%S"))+2)%2
        # rand_val = sample([2,4],1)[0]# This is randomization usind random module.
        rand_val = [2,4][index_of_rand_val]# This is randomization usind datetime module.
        self.Grid[row_index][col_index] = rand_val
        
    # An static method for checking is user has enterd an correct option.
    @staticmethod    
    def Check_options(extent,current_option):
        return current_option in list(range(1,extent+1))
        
                   
           
        
        
if __name__ == '__main__':
    Game() #Initializing the game.

    

    
