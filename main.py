import pygame
from pygame import Color


class Chip:
    def __init__(self):
        self.column = None
        self.row = None
            
            
    def draw(self, game_controller): 
        #refactor screen to be a property of Game_Controller
        # this is bad; can't assign type to game_controller, but can pass it as a parameter without error
        
        #update - error has happened regardless; fml
        
        # can't place Game_Controller above this because it references Chip
        # there must be a better way of doing this I am unaware of
        scale = game_controller.scale
        pygame.draw.ellipse(game_controller.screen, self.color, (self.column*scale + 5, self.row*scale + 5, scale - 10, scale-10))
        
        
class Game_Controller:
    def __init__(self) -> None:
        self.reset()
        

    def reset(self):
        self.game_state = {
            0: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
            1: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
            2: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
            3: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
            4: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
            5: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
            6: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}  
        }
        
        self.columns = 7
        self.rows = 6
        self.scale = 100
        self.screen = pygame.display.set_mode((self.columns * self.scale, self.rows * self.scale))
        self.screen.fill((100, 100, 100))
    
    
    def check_win(self, chip: Chip):
        test_list = []
        # Check adjacent
        for column in range (chip.column - 4, chip.column + 4):
            if column >= 0 and column < self.columns:
                test_list.append(self.game_state[column][chip.row])
                
        test_list = clean_list(test_list)
                
        is_winner(test_list, chip.team)
        test_list.clear()
        # Check vertical
                
        test_list = list(self.game_state[chip.column].values())
            
        test_list = clean_list(test_list)
            
        is_winner(test_list, chip.team)
        test_list.clear()
        
        # Check y = -x
        for i in range (-4, 4):
            if chip.column + i >= 0 and chip.row + i >=0 and chip.column + i < self.columns and chip.row + i < self.rows:
                test_list.append(self.game_state[chip.column + i][chip.row + i])
                
        test_list = clean_list(test_list)
        is_winner(test_list, chip.team)
        test_list.clear()
        
        # Check y = x
        for i in range (-4, 4):
            if chip.column - i >= 0 and chip.row + i >=0 and chip.column - i < self.columns and chip.row + i < self.rows:
                test_list.append(self.game_state[chip.column - i][chip.row + i])
                
        test_list = clean_list(test_list)
        is_winner(test_list, chip.team)
        test_list.clear()
    
            
def clean_list(test_list: list) -> list:
    for n in enumerate(test_list):
        if n[1] is None:
            continue
        else:
            test_list[n[0]] = test_list[n[0]].team
    return test_list
                

def is_winner(test_list: list, team: str):
    
    counter = 0
    memory = None
    for n in test_list:
        if n is None:
            counter = 0
        elif n == team:
            counter += 1
        else:
            counter = 0
            memory = n
        
        if counter == 4:
            print(team.capitalize(),'Wins!')
    

    
#reset
#reward
#play(action) -> direction
#game_iteration

        
class Connect_Four_AI:
    def __init__(self) -> None:
        self.team: str
        self.last_chip = None
    
    def place_chip(self, column, game_controller: Game_Controller) -> bool:
        
        new_chip = Chip()
        new_chip.team = self.team
        new_chip.color = Color(self.team)
        
        temp_row = 0
        for row in game_controller.game_state[column]:
            if row == 0 and game_controller.game_state[column][temp_row] is not None:
                print('Column Full!')
                return False
            
            elif row + 1 >= game_controller.rows or game_controller.game_state[column][row+1] is not None:
                new_chip.column = column
                new_chip.row = row
                self.last_chip = new_chip
                game_controller.game_state[column][temp_row] = new_chip
                return True
                
            elif game_controller.game_state[column][row+1] is None:
                temp_row += 1
                
            else: 
                print('error')
                return False
        
            

        pass
    
    


def main():

    pygame.init()
    
    master_controller = Game_Controller()
    player1 = Connect_Four_AI()
    player1.team = 'yellow'
    player2 = Connect_Four_AI()
    player2.team ='red'

    
             
    running = True
    
    active_player = player1
    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                
            # test Game_Controller.reset()
            if event.type == pygame.KEYDOWN:
                if event.unicode == 'r':
                    master_controller.reset()
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_column = event.__dict__['pos'][0] // master_controller.scale
                #print('Mouse column:', mouse_column) # debug line
                
                active_player.place_chip(mouse_column, master_controller)
                master_controller.check_win(active_player.last_chip)
                if active_player is player1:
                    active_player = player2
                else:
                    active_player = player1
                    
        # clear screen
        pygame.draw.rect(master_controller.screen,(100, 100, 90), [0, 0 , master_controller.columns * master_controller.scale, master_controller.rows * master_controller.scale])
        for column in master_controller.game_state:
            for row in master_controller.game_state[column]:
                if master_controller.game_state[column][row] is not None:
                    
                    master_controller.game_state[column][row].draw(master_controller)

        
        pygame.display.flip()
        
if __name__=="__main__":
    main()
    